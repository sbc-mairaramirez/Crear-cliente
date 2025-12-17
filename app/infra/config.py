import os

# Lee la variable de entorno DATABASE_URL, que contiene la URL de la base de datos
DATABASE_URL = os.getenv("DATABASE_URL")

# Si no está configurada, lanza un error
if not DATABASE_URL:
    raise RuntimeError(
        "DATABASE_URL no está configurada. Establécela como variable de entorno."
    )
