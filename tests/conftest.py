import pytest

@pytest.fixture(autouse=True)
def clean_database():
    # Fixture vacío para evitar conexión real a la BD durante los tests
    yield
