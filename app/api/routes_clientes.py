from fastapi import APIRouter, HTTPException
from app.application.create_customer_use_case import CrearClienteUseCase
from app.infra.postgres.clientes_repository_pg import ClientesRepositoryPg
from app.api.schemas import ClienteRequest

router = APIRouter()

repo = ClientesRepositoryPg()
use_case = CrearClienteUseCase(repo)

@router.post("/clientes/")
def crear_cliente(cliente: ClienteRequest):
    try:
        result = use_case.execute(cliente.model_dump())
        return {
            "mensaje": "Cliente creado exitosamente",
            "cliente": result
        }
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
