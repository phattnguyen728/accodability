from fastapi import (
    APIRouter,
    Depends,
    Response,
    Request,
    status,
    HTTPException,
)
from typing import List, Optional
from queries.pool import pool
from queries.users import UserOut, UserIn, UserQueries
from jwtdown_fastapi.authentication import Token
from authenticator import authenticator
from pydantic import BaseModel
from .users import UserToken, HttpError

from queries.friends import FriendQueries

router = APIRouter()


async def get_current_user_id(
    token: UserToken = Depends(authenticator.get_current_account_data),
):
    print(token)
    sender_id = token["user"]["id"]
    return sender_id


@router.post("/friends/{receiver_id}")
async def send_friend_request(
    receiver_id: int,
    sender_id: UserToken = Depends(authenticator.get_current_account_data),
    token: UserToken = Depends(authenticator.get_current_account_data),
    user: UserQueries = Depends(),
    friends: FriendQueries = Depends(),
):
    # print(token)
    # sender_id = token["user"]["id"]
    request_id = friends.send_friend_request(sender_id, receiver_id)
    try:
        # request_id.send_friend_request(sender_id, receiver_id)
        request_id
        return {
            "Message": " Friend request sent successfully",
            # "request_id": request_id,
        }
    except Exception as e:
        errorMessage = f"Error Message is {str(e)}"
        return {"error": errorMessage}


# @router.get("/friends/3")
# async def get_pending_friend_requests(
#     user_data: dict = Depends(get_current_user_id),
#     friends: FriendQueries = Depends(authenticator.get_current_account_data),
# ):
#     if user_data is None:
#         raise HTTPException(
#             status_code=401, detail="User information not found in token"
#         )

#     pending_requests = friends.get_pending_friend_requests(user_data)
#     return {"pending_requests": pending_requests}
