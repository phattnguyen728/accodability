import pytest
from fastapi.testclient import TestClient
from main import app
from authenticator import authenticator
from pydantic import BaseModel


@pytest.fixture
def client():
    return TestClient(app)


class UserToken(BaseModel):
    access_token: str
    token_type: str
    user: dict


def fake_get_current_account_data():
    return UserToken(
        access_token="test_token",
        token_type="Bearer",
        user={
            "id": "1",
            "first_name": "John",
            "last_name": "Doe",
            "username": "johndoe",
            "email": "johndoe@example.com",
        },
    )


def test_get_messages(client):
    user_token = fake_get_current_account_data()

    app.dependency_overrides[
        authenticator.get_current_account_data
    ] = lambda: user_token.user

    response = client.get("/messages")
    app.dependency_overrides = {}
    assert response.status_code == 200
    assert "Message Inbox" in response.json()
