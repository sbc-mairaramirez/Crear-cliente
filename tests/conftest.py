import pytest

@pytest.fixture(autouse=True)
def clean_database():
    """
    Fixture que evita que se utilice la base de datos real durante los tests.
    """
    yield
