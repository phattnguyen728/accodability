from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
)
from authenticator import authenticator
from .users import UserToken

from queries.friends import FriendQueries

router = APIRouter()


@router.post("/friends")
async def send_friend_request(
    receiver_id: int,
    sender: UserToken = Depends(authenticator.get_current_account_data),
    friends: FriendQueries = Depends(),
):
    sender_id = sender["id"]
    print(sender_id)
    # print(token)
    # sender_id = token["user"]["id"]
    try:
        # request_id.send_friend_request(sender_id, receiver_id)
        friends.send_friend_request(sender_id, receiver_id)
        return {
            "Message": " Friend request sent successfully",
        }
    except Exception as e:
        errorMessage = f"Error Message is {str(e)}"
        return {"error": errorMessage}


async def get_current_user_id(
    token: UserToken = Depends(authenticator.get_current_account_data),
):
    print(token)
    sender_id = token["user"]["id"]
    return sender_id


@router.get("/friends")
async def get_pending_friend_requests(
    # id#1
    user: UserToken = Depends(authenticator.get_current_account_data),
    friends: FriendQueries = Depends(),
):
    user_id = user["id"]
    # 1
    # return print(user_id)
    if user is None:
        raise HTTPException(
            status_code=401, detail="User information not found in token"
        )
    pending_requests = friends.get_pending_friend_requests(user_id)
    return {"pending_requests": pending_requests}
