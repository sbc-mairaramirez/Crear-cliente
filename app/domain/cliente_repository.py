from abc import ABC, abstractmethod
from app.domain.cliente import Cliente

class ClienteRepositoryInterface(ABC):

    @abstractmethod
    def exists_email(self, email: str) -> bool:
        pass

    @abstractmethod
    def create_customer(self, cliente: Cliente) -> Cliente:
        pass
