from fastapi import FastAPI
from app.api.routes_clientes import router as cliente_router

app = FastAPI()

app.include_router(cliente_router)   # ← IMPORTANTE
