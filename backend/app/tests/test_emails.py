import pytest
from httpx import AsyncClient
from fastapi import status

from app.main import app

pytestmark = pytest.mark.asyncio

@pytest.fixture
def email_payload():
    return {
        "subject": "Test Email",
        "sender": "test@example.com",
        "recipient": "recipient@example.com",
        "content": "Test email content",
        "status": "pending"
    }

async def test_create_email(client, email_payload):
    response = await client.post("/api/v1/emails/", json=email_payload)
    assert response.status_code == status.HTTP_201_CREATED
    data = response.json()
    assert data["subject"] == email_payload["subject"]
    assert data["sender"] == email_payload["sender"]
    assert "id" in data

async def test_get_email(client, email_payload):
    # Primeiro cria um email
    create_response = await client.post("/api/v1/emails/", json=email_payload)
    email_id = create_response.json()["id"]
    
    # Depois busca o email criado
    response = await client.get(f"/api/v1/emails/{email_id}")
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert data["id"] == email_id
    assert data["subject"] == email_payload["subject"]

async def test_list_emails(client, email_payload):
    # Cria alguns emails
    await client.post("/api/v1/emails/", json=email_payload)
    await client.post("/api/v1/emails/", json=email_payload)
    
    # Lista todos os emails
    response = await client.get("/api/v1/emails/")
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert len(data) >= 2

async def test_update_email(client, email_payload):
    # Cria um email
    create_response = await client.post("/api/v1/emails/", json=email_payload)
    email_id = create_response.json()["id"]
    
    # Atualiza o email
    update_data = {"subject": "Updated Subject"}
    response = await client.patch(f"/api/v1/emails/{email_id}", json=update_data)
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert data["subject"] == "Updated Subject"

async def test_delete_email(client, email_payload):
    # Cria um email
    create_response = await client.post("/api/v1/emails/", json=email_payload)
    email_id = create_response.json()["id"]
    
    # Deleta o email
    response = await client.delete(f"/api/v1/emails/{email_id}")
    assert response.status_code == status.HTTP_204_NO_CONTENT
    
    # Verifica se foi realmente deletado
    get_response = await client.get(f"/api/v1/emails/{email_id}")
    assert get_response.status_code == status.HTTP_404_NOT_FOUND 