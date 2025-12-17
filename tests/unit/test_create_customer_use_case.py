import pytest
from app.application.create_customer_use_case import CrearClienteUseCase
from app.domain.cliente import Cliente
from app.domain.cliente_repository import ClienteRepositoryInterface

class FakeRepository(ClienteRepositoryInterface):
    """
    Repositorio falso para hacer pruebas unitarias sin acceder a una base de datos real.
    """
    def __init__(self):
        self.customers = []

    def exists_email(self, email: str) -> bool:
        return any(c.email == email for c in self.customers)

    def create_customer(self, cliente: Cliente) -> Cliente:
        cliente.id = len(self.customers) + 1
        self.customers.append(cliente)
        return cliente

def test_should_fail_if_email_exists():
    """
    Test para verificar que se lanza un error si el correo electrónico ya existe.
    """
    repo = FakeRepository()
    use_case = CrearClienteUseCase(repo)

    # Agrega un cliente para que exista el correo
    repo.customers.append(Cliente(
        id=1,
        first_name="Ana",
        last_name="Lopez",
        email="ana@mail.com",
        phone="123"
    ))

    with pytest.raises(ValueError):
        use_case.execute({
            "first_name": "Ana",
            "last_name": "Lopez",
            "email": "ana@mail.com",
            "phone": "123"
        })

def test_should_create_customer_successfully():
    """
    Test para verificar que se crea un cliente correctamente.
    """
    repo = FakeRepository()
    use_case = CrearClienteUseCase(repo)

    data = {
        "first_name": "Ana",
        "last_name": "Lopez",
        "email": "ana@mail.com",
        "phone": "123"
    }

    result = use_case.execute(data)

    assert result.id == 1
    assert result.first_name == "Ana"
    assert result.email == "ana@mail.com"
