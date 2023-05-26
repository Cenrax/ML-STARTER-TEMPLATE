import pytest
import requests
from fastapi import FastAPI
from fastapi.testclient import TestClient

from main import app


@pytest.fixture
def client():
    return TestClient(app)


def test_get_value(client):
    response = client.get("/get/test_key")
    assert response.status_code == 200
    assert response.json() == {"key": "test_key", "value": "1"}




@pytest.mark.parametrize(
    "origin",
    [
        "http://localhost:3000",
        # Add additional origins if needed
    ],
)
def test_cors_middleware(client, origin):
    response = client.options(
        "/get/test_key",
        headers={"origin": origin, "access-control-request-method": "GET"},
    )
    assert response.status_code == 200
    assert response.headers["access-control-allow-origin"] == origin
    assert response.headers["access-control-allow-credentials"] == "true"
    

if __name__ == "__main__":
    pytest.main()
