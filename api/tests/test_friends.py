# # WORK IN PROGRESS***
# # from routers.friends import get_pending_friend_requests, FriendListOut
# from pydantic import BaseModel

# # from fastapi import Depends, FastAPI
# from fastapi.testclient import TestClient
# from main import app
# from queries.friends import FriendRequestOut, FriendQueries
# from queries.users import UserOut
# from authenticator import authenticator

# from typing import Annotated


# # https://fastapi.tiangolo.com/advanced/testing-dependencies/
# # app = FastAPI()


# async def common_parameters(
#     q: str | None = None, skip: int = 0, limit: int = 100
# ):
#     return {"q": q, "skip": skip, "limit": limit}


# @app.get("/friends/")
# async def read_items(commons: Annotated[dict, Depends(common_parameters)]):
#     return {"message": "list of friends here", "params": commons}


# client = TestClient(app)


# async def override_dependency(q: str | None = None):
#     return {"q": q, "skip": 5, "limit": 10}


# app.dependency_overrides[common_parameters] = override_dependency


# # replace "params" with FriendRequestOut content??
# def test_override_in_friendsList():
#     response = client.get("/items/")
#     assert response.status_code == 200
#     assert response.json() == {
#         "message": "list of friends here",
#         "params": {"q": None, "skip": 5, "limit": 10},
#     }


# #
# def fake_create_first_account():
#     return UserOut(
#         id="1",
#         first_name="john",
#         last_name="cena",
#         username="TheLegend42",
#         email="test@test.com",
#     )


# def fake_create_second_account():
#     return UserOut(
#         id="2",
#         first_name="naruto",
#         last_name="Uzimaki",
#         username="rasengan",
#         email="naruto@test.com",
#     )


# def fake_get_first_account_data():
#     return FriendRequestOut(
#         id=1,
#         sender_id="1",
#         receiver_id="2",
#         username="TheLegend42",
#         status="pending",
#     )


# def fake_get_second_account_data():
#     return FriendRequestOut(
#         id=2,
#         sender_id="2",
#         receiver_id="1",
#         username="rasengan",
#         status="pending",
#     )


# # stuff from learn vvvvvv


# def test_send_friend_request():
#     app.dependency_overrides[
#         authenticator.get_current_account_data
#     ] = fake_get_first_account_data

#     app.dependency_overrides[
#         authenticator.get_current_account_data
#     ] = fake_get_second_account_data

#     response = client.post("/friends")
#     # where sender = first account
#     # where receiver = second account
#     # where receiver_id = fake_get_second_account_data["id"]

#     app.dependency_overrides = {}
#     # wipes the memory

#     assert response.status_code == 200
#     assert response.json() == FriendListOut(thing=2)


# # def test_send_friend_request():
# #     # user_id = 1
# #     input = 1

# #     result = get_pending_friend_requests(input)

# #     assert result == 2
