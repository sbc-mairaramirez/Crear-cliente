# HU-003 – Crear Cliente

Microservicio para registrar clientes usando FastAPI, PostgreSQL y arquitectura hexagonal.

## 🚀 Arquitectura

El proyecto sigue arquitectura hexagonal:


## 🧪 Tests

- Pruebas unitarias (caso de uso)
- Pruebas de integración (endpoint real con TestClient)
- Cobertura mínima requerida: **90%**

Ejecutar tests:

```bash
pytest --maxfail=1 --disable-warnings -q
