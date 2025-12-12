from unittest.mock import MagicMock, patch
from app.infra.postgres.clientes_repository_pg import ClientesRepositoryPg
from app.domain.cliente import Cliente


@patch("app.infra.postgres.clientes_repository_pg.DatabaseConnection")
def test_exists_email(mock_db):
    mock_conn = MagicMock()
    mock_cursor = MagicMock()

    mock_cursor.fetchone.return_value = (1,)
    mock_conn.cursor.return_value = mock_cursor
    mock_db.return_value.get_connection.return_value = mock_conn

    repo = ClientesRepositoryPg()
    result = repo.exists_email("test@example.com")

    assert result is True
    mock_cursor.execute.assert_called_once()


@patch("app.infra.postgres.clientes_repository_pg.DatabaseConnection")
def test_create_customer(mock_db):
    mock_conn = MagicMock()
    mock_cursor = MagicMock()

    mock_cursor.fetchone.return_value = (1, "2025-01-01")
    mock_conn.cursor.return_value = mock_cursor
    mock_db.return_value.get_connection.return_value = mock_conn

    cliente = Cliente(first_name="Ana", last_name="Perez", email="ana@example.com")

    repo = ClientesRepositoryPg()
    result = repo.create_customer(cliente)

    assert result.id == 1
    mock_cursor.execute.assert_called_once()
    mock_conn.commit.assert_called_once()
