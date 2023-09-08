import pytest
from fastapi.testclient import TestClient
from main import app
from authenticator import authenticator
from pydantic import BaseModel
from queries.posts import PostQueries


@pytest.fixture
def client():
    return TestClient(app)


class UserToken(BaseModel):
    access_token: str
    token_type: str
    user: dict


def fake_get_current_account_data():
    return (
        {
            "id": "1",
            "first_name": "John",
            "last_name": "Doe",
            "username": "johndoe",
            "email": "johndoe@example.com",
        },
    )


class FakePostQueries:
    # def get_posts(self) -> List[Dict[str, str]]:
    #     return []

    def test_get_all_posts(client):
        app.dependency_overrides[
            authenticator.get_current_account_data
        ] = fake_get_current_account_data
        json = {}
        expected = [
            {},
        ]
        app.dependency_overrides[PostQueries] = FakePostQueries
        response = client.get("/posts", json=json)
        app.dependency_overrides = {}
        assert response.status_code == 200
        assert response.json() == expected

    # def create_post(self, author_id, post_data) -> Dict[str, str]:
    #     body = post_data.get("body")
    #     created_at = datetime(2023, 1, 1)
    #     return {
    #         "id": 1,
    #         "author_id": author_id,
    #         "body": body,
    #         "created_at": created_at,
    #     }

    # def delete_post(self, post_id) -> bool:
    #     return True

    # def update_post(self, post_id, updated_post_data) -> Dict[str, str]:
    #     body = updated_post_data.get("body")
    #     created_at = datetime(2023, 1, 1)
    #     return {
    #         "id": post_id,
    #         "author_id": updated_post_data.get("author_id"),
    #         "body": body,
    #         "created_at": created_at,
    #     }


# def test_get_all_posts(client):
#     app.dependency_overrides[
#         authenticator.get_current_account_data
#     ] = fake_get_current_account_data
#     app.dependency_overrides[FakePostQueries] = FakePostQueries
#     response = client.get("/api/posts")
#     app.dependency_overrides = {}
#     assert response.status_code == 200
#     assert response.json() == []


# def test_create_post(client):
#     app.dependency_overrides[
#         authenticator.get_current_account_data
#     ] = fake_get_current_account_data
#     app.dependency_overrides[FakePostQueries] = FakePostQueries
#     response = client.post("/api/posts", json={"body": "Test post"})
#     app.dependency_overrides = {}
#     assert response.status_code == 201
#     assert response.json() == {"id": 1, "author_id": "1", "body": "Test post"}


# def test_update_post(client):
#     app.dependency_overrides[
#         authenticator.get_current_account_data
#     ] = fake_get_current_account_data
#     app.dependency_overrides[FakePostQueries] = FakePostQueries
#     response = client.put("/api/posts/1", json={"author_id": "1", "body": "Updated post"})
#     app.dependency_overrides = {}
#     assert response.status_code == 200
#     assert response.json() == {"id": 1, "author_id": "1", "body": "Updated post"}


# def test_delete_post(client):
#     app.dependency_overrides[
#         authenticator.get_current_account_data
#     ] = fake_get_current_account_data
#     app.dependency_overrides[FakePostQueries] = FakePostQueries
#     response = client.delete("/api/posts/1")
#     app.dependency_overrides = {}
#     assert response.status_code == 200
#     assert response.json() == {"status": "success", "message": "Post 1 deleted successfully"}
