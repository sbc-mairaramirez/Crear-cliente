from app.infra.database import DatabaseConnection
from app.domain.cliente import Cliente
from app.domain.cliente_repository import ClienteRepositoryInterface


class ClientesRepositoryPg(ClienteRepositoryInterface):

    def exists_email(self, email: str) -> bool:
        conn = DatabaseConnection().get_connection()
        cur = conn.cursor()

        # FIX: la tabla correcta es customers
        cur.execute("SELECT id FROM customers WHERE email = %s", (email,))
        result = cur.fetchone()

        cur.close()
        conn.close()

        return result is not None

    def create_customer(self, cliente: Cliente) -> Cliente:
        conn = DatabaseConnection().get_connection()
        cur = conn.cursor()

        query = """
            INSERT INTO customers (first_name, last_name, email, phone)
            VALUES (%s, %s, %s, %s)
            RETURNING id, created_at;
        """

        cur.execute(query, (
            cliente.first_name,
            cliente.last_name,
            cliente.email,
            cliente.phone
        ))

        cliente.id, cliente.created_at = cur.fetchone()

        conn.commit()
        cur.close()
        conn.close()

        return cliente
