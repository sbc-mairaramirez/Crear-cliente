from fastapi import APIRouter, HTTPException
from app.application.create_customer_use_case import CrearClienteUseCase
from app.domain.cliente import Cliente
from app.infra.postgres.clientes_repository_pg import ClientesRepositoryPg

router = APIRouter()

repo = ClientesRepositoryPg()
use_case = CrearClienteUseCase(repo)

@router.post("/clientes/")
def crear_cliente(cliente: Cliente):
    try:
        return use_case.execute(cliente.model_dump())
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
