from app.domain.cliente_repository import ClienteRepositoryInterface
from app.domain.cliente import Cliente

class CrearClienteUseCase:

    def __init__(self, repo: ClienteRepositoryInterface):
        self.repo = repo

    def execute(self, data: dict):

        required_fields = ["first_name", "last_name", "email"]
        for field in required_fields:
            if not data.get(field):
                raise ValueError("Debe ingresar todos los campos obligatorios")

        email = data["email"]

        if self.repo.exists_email(email):
            raise ValueError("El correo electrónico ya existe")

        cliente = Cliente(
            first_name=data["first_name"],
            last_name=data["last_name"],
            email=data["email"],
            phone=data.get("phone")
        )

        return self.repo.create_customer(cliente)
