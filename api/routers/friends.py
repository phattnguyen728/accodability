from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
)
from authenticator import authenticator
from .users import UserToken

from queries.friends import (
    FriendQueries,
    FriendRequestIn,
    FriendRequestApprove,
)

router = APIRouter()


@router.post("/friends")
async def send_friend_request(
    friend_request_form: FriendRequestIn,
    sender: UserToken = Depends(authenticator.get_current_account_data),
    friends: FriendQueries = Depends(),
):
    sender_id = sender["id"]
    receiver_id = friend_request_form.receiver_id
    try:
        friends.send_friend_request(sender_id, receiver_id)
        return {
            "Friend Request Message": "Friend request sent successfully",
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
    user: UserToken = Depends(authenticator.get_current_account_data),
    friendList: FriendQueries = Depends(),
):
    user_id = user["id"]
    if user is None:
        raise HTTPException(
            status_code=401, detail="User information not found in token"
        )
    friends = friendList.get_pending_friend_requests(user_id)
    return friends


@router.put("/friends/{sender_id}")
async def accept_friend_request(
    approve: FriendRequestApprove,
    user: UserToken = Depends(authenticator.get_current_account_data),
    friendList: FriendQueries = Depends(),
):
    sender_id = approve.sender_id
    receiver_id = approve.receiver_id
    if user is None:
        raise HTTPException(
            status_code=401, detail="User information not found in token"
        )
    status = friendList.approve_friend_request(sender_id, receiver_id)
    return status
