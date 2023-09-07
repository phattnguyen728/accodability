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


def test_create_post(client):
    user_token = fake_get_current_account_data()
    app.dependency_overrides[
        authenticator.get_current_account_data
    ] = lambda: user_token.user

    post_data = {
        "title": "Test Post",
        "body": "This is a test post.",
        "hyperlink": "https://example.com",
        "author_id": 1,
    }

    response = client.post("/api/posts", json=post_data)
    app.dependency_overrides = {}
    assert response.status_code == 200
    assert "id" in response.json()
    assert response.json()["title"] == post_data["title"]


def test_get_post_by_id(client):
    post_id_to_test = 1
    response = client.get(f"/api/posts/{post_id_to_test}")
    assert response.status_code == 200
    assert "id" in response.json()
    assert response.json()["id"] == post_id_to_test


def test_get_all_posts(client):
    user_token = fake_get_current_account_data()
    app.dependency_overrides[
        authenticator.get_current_account_data
    ] = lambda: user_token.user

    response = client.get("/api/posts")

    app.dependency_overrides = {}

    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_delete_post(client):
    user_token = fake_get_current_account_data()
    app.dependency_overrides[
        authenticator.get_current_account_data
    ] = lambda: user_token.user

    post_id_to_test = 1
    response = client.delete(f"/api/posts/{post_id_to_test}")

    app.dependency_overrides = {}

    assert response.status_code == 200
    assert response.json() is True

# still working on update post
# def test_update_post(client):
#     user_token = fake_get_current_account_data()
#     app.dependency_overrides[
#         authenticator.get_current_account_data
#     ] = lambda: user_token.user

#     post_id_to_test = 3
#     updated_post_data = {
#         "title": "Updated Test Post",
#         "body": "This is an updated test post.",
#         "hyperlink": "https://updated-example.com",
#     }

#     response = client.put(f"/api/posts/{post_id_to_test}", json=updated_post_data)

#     app.dependency_overrides = {}

#     assert response.status_code == 200
#     assert "id" in response.json()
#     assert response.json()["title"] == updated_post_data["title"]
