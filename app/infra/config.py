import os

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://postgres:14082006@localhost:5432/customer_registry_db"
)
