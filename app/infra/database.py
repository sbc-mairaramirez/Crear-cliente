import os
import psycopg2
from psycopg2.extras import RealDictCursor
from app.infra.config import DATABASE_URL

try:
    from dotenv import load_dotenv
    load_dotenv()
except Exception:
    pass

class DatabaseConnection:
    def __init__(self):
        # Si DATABASE_URL está presente, úsalo (psycopg2 accepts dsn)
        dsn = os.getenv("DATABASE_URL", DATABASE_URL)
        # si tienes variables separadas (opcionales) podrías construir conn_args
        self.connection = psycopg2.connect(dsn)
        self.connection.autocommit = False  # gestionar commit/rollback en repo

    def get_connection(self):
        return self.connection

    def get_cursor(self):
        return self.connection.cursor(cursor_factory=RealDictCursor)
