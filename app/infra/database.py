import os
import psycopg2
from psycopg2.extras import RealDictCursor
from app.infra.config import DATABASE_URL

class DatabaseConnection:
    """
    Clase encargada de establecer la conexión con la base de datos PostgreSQL.
    """
    def __init__(self):
        # Si DATABASE_URL está presente, úsalo para conectar
        dsn = os.getenv("DATABASE_URL", DATABASE_URL)
        self.connection = psycopg2.connect(dsn)
        self.connection.autocommit = False  # Manejo manual de commit/rollback

    def get_connection(self):
        """
        Devuelve la conexión de la base de datos.
        """
        return self.connection

    def get_cursor(self):
        """
        Devuelve un cursor con formato de diccionario.
        """
        return self.connection.cursor(cursor_factory=RealDictCursor)
