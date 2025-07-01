import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from fastapi.testclient import TestClient
from main import app


client = TestClient(app)

def test_get_classes():
    response = client.get("/classes")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_book_class_success():
    payload = {
        "class_id": "1",
        "client_name": "John Doe",
        "client_email": "john@example.com"
    }
    response = client.post("/book", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["client_email"] == "john@example.com"

def test_bookings_by_email():
    response = client.get("/bookings", params={"client_email": "john@example.com"})
    assert response.status_code == 200
    assert isinstance(response.json(), list)
