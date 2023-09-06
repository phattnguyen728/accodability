from fastapi.testclient import TestClient
from authenticator import authenticator

from main import app

from queries.users import UserOut
from queries.comments import CommentIn, CommentOut, CommentQueries, CommentEdit
from datetime import datetime

client = TestClient(app)


def fake_get_current_account_data():
    return {
        "id": 1,
        "first_name": "Test",
        "last_name": "User",
        "username": "TestUser",
        "email": "TestUser@gmail.com",
    }


class FakeCommentQueries:
    def get_comments(self, post_id):
        return []

    def create_comment(self, post_id, author_id, comment=CommentIn):
        body = comment.body
        created_at = datetime(2023, 1, 1)
        return CommentOut(
            id=1,
            author_id=author_id,
            post_id=post_id,
            body=body,
            created_at=created_at,
        )

    def delete_comment(self, id, author_id, post_id):
        return True

    def update_comment(self, id, post_id, author_id, comment=CommentEdit):
        body = comment.body
        created_at = datetime(2023, 1, 1)
        return CommentOut(
            id=id,
            author_id=author_id,
            post_id=post_id,
            body=body,
            created_at=created_at,
        )

    def get_comments_by_user(self, author_id):
        return []


def test_get_all_comments():
    app.dependency_overrides[
        authenticator.get_current_account_data
    ] = fake_get_current_account_data
    app.dependency_overrides[CommentQueries] = FakeCommentQueries
    response = client.get("/api/posts/1/comments")
    app.dependency_overrides = {}
    assert response.status_code == 200
    assert response.json() == []


def test_create_comment():
    app.dependency_overrides[
        authenticator.get_current_account_data
    ] = fake_get_current_account_data
    app.dependency_overrides[CommentQueries] = FakeCommentQueries
    json = {"author_id": 1, "post_id": 1, "body": "Test Comment"}
    expected = {
        "id": 1,
        "author_id": 1,
        "post_id": 1,
        "body": "Test Comment",
        "created_at": "2023-01-01T00:00:00",
    }
    response = client.post("/api/posts/1/comments", json=json)
    app.dependency_overrides = {}
    assert response.status_code == 200
    assert response.json() == expected


def test_delete_comment():
    app.dependency_overrides[
        authenticator.get_current_account_data
    ] = fake_get_current_account_data
    app.dependency_overrides[CommentQueries] = FakeCommentQueries
    response = client.delete("/api/posts/1/comments/1")
    app.dependency_overrides = {}
    assert response.status_code == 200
    assert response.json() == True


def test_update_comment():
    app.dependency_overrides[
        authenticator.get_current_account_data
    ] = fake_get_current_account_data
    app.dependency_overrides[CommentQueries] = FakeCommentQueries
    json = {
        "id": 1,
        "author_id": 1,
        "post_id": 1,
        "body": "Test Comment Updated",
    }
    expected = {
        "id": 1,
        "author_id": 1,
        "post_id": 1,
        "body": "Test Comment Updated",
        "created_at": "2023-01-01T00:00:00",
    }
    response = client.put("/api/posts/1/comments/1", json=json)
    app.dependency_overrides = {}
    assert response.status_code == 200
    assert response.json() == expected


def test_get_comments_by_user():
    app.dependency_overrides[
        authenticator.get_current_account_data
    ] = fake_get_current_account_data
    app.dependency_overrides[CommentQueries] = FakeCommentQueries
    response = client.get("/api/users/1/comments/")
    app.dependency_overrides = {}
    assert response.status_code == 200
    assert response.json() == []
