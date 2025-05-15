import pytest
from fastapi.testclient import TestClient
from unittest.mock import AsyncMock, patch
from app.main import app
from httpx import AsyncClient


client = TestClient(app)

@pytest.mark.asyncio
@patch("app.api.endpoints.cafes.get_connection")
async def test_get_all_cafes(mock_get_connection):
    # Create a fake asyncpg connection object with fetch method
    mock_conn = AsyncMock()
    mock_conn.fetch.return_value = [
        {"id": 1, "name": "Cafe A", "city": "Kathmandu", "has_wifi": True, "rating": 4.5},
        {"id": 2, "name": "Cafe B", "city": "Pokhara", "has_wifi": False, "rating": 3.7}
    ]
    mock_get_connection.return_value = mock_conn

    response = client.get("/cafes/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) == 2
    assert data[0]["name"] == "Cafe A"



#  
def test_create_cafe(mocker):
    # Create an async mock connection
    mock_conn = AsyncMock()

    # Mock fetchrow return value
    mock_conn.fetchrow.return_value = {
        "id": 1,
        "name": "Test Cafe",
        "city": "Kathmandu",
        "has_wifi": True,
        "rating": 4
    }

    # Patch get_connection with mocked async connection
    mocker.patch("app.api.endpoints.cafes.get_connection", return_value=mock_conn)

    payload = {
        "name": "Test Cafe",
        "city": "Kathmandu",
        "has_wifi": True,
        "rating": 4
    }

    response = client.post("/cafes/addcafe", json=payload)
    
    print('string1',response.status_code)
    print('string2', response.json())


    assert response.status_code == 201
    assert response.json()["name"] == "Test Cafe"