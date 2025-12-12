from app.domain.cliente import Cliente

def test_cliente_model():
    cliente = Cliente(
        first_name="Ana",
        last_name="Perez",
        email="ana@example.com",
        phone="123"
    )

    assert cliente.first_name == "Ana"
    assert cliente.email == "ana@example.com"
    assert cliente.phone == "123"
