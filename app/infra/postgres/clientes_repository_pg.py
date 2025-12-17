from app.infra.database import DatabaseConnection
from app.domain.cliente import Cliente
from app.domain.cliente_repository import ClienteRepositoryInterface

class ClientesRepositoryPg(ClienteRepositoryInterface):
    """
    Repositorio que maneja las operaciones con la base de datos PostgreSQL.
    """

    def exists_email(self, email: str) -> bool:
        """
        Verifica si un correo electrónico ya está registrado en la base de datos.
        """
        conn = DatabaseConnection().get_connection()
        cur = conn.cursor()

        # Consulta a la base de datos para verificar si existe el correo
        cur.execute("SELECT id FROM customers WHERE email = %s", (email,))
        result = cur.fetchone()

        cur.close()
        conn.close()

        return result is not None

    def create_customer(self, cliente: Cliente) -> Cliente:
        """
        Crea un cliente en la base de datos y devuelve el objeto con el id asignado.
        """
        conn = DatabaseConnection().get_connection()
        cur = conn.cursor()

        query = """
            INSERT INTO customers (first_name, last_name, email, phone)
            VALUES (%s, %s, %s, %s)
            RETURNING id, created_at;
        """

        # Ejecuta la consulta SQL para insertar al cliente
        cur.execute(query, (
            cliente.first_name,
            cliente.last_name,
            cliente.email,
            cliente.phone
        ))

        # Asigna el id y la fecha de creación al objeto cliente
        cliente.id, cliente.created_at = cur.fetchone()

        # Realiza el commit y cierra la conexión
        conn.commit()
        cur.close()
        conn.close()

        return cliente
