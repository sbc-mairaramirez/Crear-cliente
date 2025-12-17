from fastapi.testclient import TestClient
from main import app
from app.domain.cliente import Cliente

client = TestClient(app)

def test_post_crear_cliente_ok():
    """
    Test para verificar que la API crea un cliente correctamente.
    """
    payload = {
        "first_name": "Test",
        "last_name": "User",
        "email": "unique_123@test.com",
        "phone": "111222333"
    }

    res = client.post("/clientes/", json=payload)

    assert res.status_code == 200
    json = res.json()
    
    assert "id" in json
    assert json["first_name"] == "Test"
    assert json["email"] == "unique_123@test.com"

def test_post_email_duplicado():
    """
    Test para verificar que la API lanza un error si el correo ya existe.
    """
    payload = {
        "first_name": "Test",
        "last_name": "User",
        "email": "duplicate@test.com",
        "phone": "111222333"
    }

    # Primer POST — debe funcionar
    client.post("/clientes/", json=payload)

    # Segundo POST — debe fallar
    res2 = client.post("/clientes/", json=payload)

    assert res2.status_code == 400
