import pytest
from fastapi.testclient import TestClient
from main import app
from authenticator import authenticator
from pydantic import BaseModel
from queries.friends import (
    FriendQueries,
    FriendRequestOut,
)


@pytest.fixture
def client():
    return TestClient(app)


class UserToken(BaseModel):
    access_token: str
    token_type: str
    user: dict


def fake_get_first_account_data():
    return {
        "id": "1",
        "first_name": "John",
        "last_name": "Cena",
        "username": "johncena",
        "email": "johncena@test.com",
    }
    # return UserToken(
    #     access_token="test_token_1",
    #     token_type="Bearer",
    #     user={
    #         "id": "1",
    #         "first_name": "John",
    #         "last_name": "Cena",
    #         "username": "johncena",
    #         "email": "johncena@test.com",
    #     },
    # )


# def fake_get_second_account_data():
#     return UserToken(
#         access_token="test_token_2",
#         token_type="Bearer",
#         user={
#             "id": "2",
#             "first_name": "Naruto",
#             "last_name": "Uzimaki",
#             "username": "narutouzimaki",
#             "email": "naruto@konoha.com",
#         },
#     )


class FakeFriendQueries:
    def send_friend_request(self, sender_id, receiver_id):
        return FriendRequestOut(
            id=1,
            sender_id=1,
            receiver_id=2,
            status="pending",
        )

    def get_pending_friend_requests(self, user_id):
        return [
            {
                "id": 2,
                "receiver_id": 1,
                "sender_id": 2,
                "status": "pending",
            }
        ]


def test_send_friend_request(client):
    # user_token_1 = fake_get_first_account_data()
    app.dependency_overrides[
        authenticator.get_current_account_data
    ] = fake_get_first_account_data
    app.dependency_overrides[FriendQueries] = FakeFriendQueries

    json = {"sender_id": 1, "receiver_id": 2}
    expected = {"Friend Request Message": "Friend request sent successfully"}

    response = client.post("/friends", json=json)

    app.dependency_overrides = {}
    assert response.status_code == 200
    assert response.json() == expected


def test_get_friend_list(client):
    # user_token = fake_get_first_account_data()

    # app.dependency_overrides[
    #     authenticator.get_current_account_data
    # ] = lambda: user_token.user
    app.dependency_overrides[
        authenticator.get_current_account_data
    ] = fake_get_first_account_data
    app.dependency_overrides[FriendQueries] = FakeFriendQueries
    response = client.get("/friends")
    app.dependency_overrides = {}
    assert response.status_code == 200
    expected = [
        {"id": 2, "receiver_id": 1, "sender_id": 2, "status": "pending"}
    ]
    assert response.json() == expected
