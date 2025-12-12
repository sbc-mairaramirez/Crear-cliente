import pytest
from unittest.mock import MagicMock
from app.application.create_customer_use_case import CrearClienteUseCase
from app.domain.cliente import Cliente


def test_crear_cliente_exitoso():
    repo = MagicMock()
    repo.exists_email.return_value = False
    repo.create_customer.return_value = Cliente(
        id=1, first_name="Ana", last_name="Perez", email="ana@example.com"
    )

    use_case = CrearClienteUseCase(repo)

    data = {
        "first_name": "Ana",
        "last_name": "Perez",
        "email": "ana@example.com"
    }

    result = use_case.execute(data)

    assert result.id == 1
    repo.exists_email.assert_called_once()
    repo.create_customer.assert_called_once()


def test_crear_cliente_falta_campo():
    repo = MagicMock()
    use_case = CrearClienteUseCase(repo)

    data = {
        "first_name": "Ana",
        "email": "ana@example.com"
    }

    with pytest.raises(ValueError) as exc:
        use_case.execute(data)

    assert "Missing required field" in str(exc.value)


def test_crear_cliente_email_existente():
    repo = MagicMock()
    repo.exists_email.return_value = True

    use_case = CrearClienteUseCase(repo)

    data = {
        "first_name": "Ana",
        "last_name": "Perez",
        "email": "ana@example.com"
    }

    with pytest.raises(ValueError) as exc:
        use_case.execute(data)

    assert "email already exists" in str(exc.value).lower()
