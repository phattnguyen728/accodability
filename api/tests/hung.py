# from pydantic import BaseModel
from fastapi.testclient import TestClient
from main import app
from unittest.mock import MagicMock
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
    user = UserOut(
        id=1,
        first_name="phat",
        last_name="nguyen",
        username="phatnguyen",
        email="phat@test.com",
    )
    return user


class TestUserQuery:
    def get_all(self):
        return []


def test_get_all_users(monkeypatch):
    monkeypatch.setattr(
        "app.authenticator.get_current_account_data",
        MagicMock(return_value=test_user_data()),
    )
    monkeypatch.setattr("app.queries.users.UserQueries", TestUserQuery)

    response = client.get("/users")

    assert response.status_code == 200
    assert response.json() == []


def test_get_all_users():
    app.dependency_overrides[UserQueries] = TestUserQuery
    app.dependency_overrides[
        authenticator.get_current_account_data
    ] = test_user_data

    response = client.get("/users")

    app.dependency_overrides = {}

    assert response.status_code == 200
    # assert response.status_code == status.HTTP_200_OK
    assert response.json() == []
    # assert response.json() == []
