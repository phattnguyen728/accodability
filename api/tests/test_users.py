from pydantic import BaseModel
from fastapi.testclient import TestClient

from main import app
from authenticator import authenticator
from queries.users import UserQueries

client = TestClient(app)


class EmptyUserQueries:
    def get_users(self):
        return []


class UserOut(BaseModel):
    id: str
    first_name: str
    last_name: str
    username: str
    email: str


def test_user_data():
    account_data = {
        "id": "1",
        "first_name": "phat",
        "last_name": "nguyen",
        "username": "phatnguyen",
        "email": "phat@test.com",
    }

    assert account_data["id"] == "1"
    assert account_data["first_name"] == "phat"
    assert account_data["last_name"] == "nguyen"
    assert account_data["username"] == "phatnguyen"
    assert account_data["email"] == "phat@test.com"


class TestUserQuery:
    def get_all(self):
        return []


def test_get_all_users():
    app.dependency_overrides[UserQueries] = TestUserQuery
    app.dependency_overrides[
        authenticator.get_current_account_data
    ] = test_user_data
    response = client.get("/users")
    app.dependency_overrides = {}
    assert response.status_code == 200
    assert response.json() == []
