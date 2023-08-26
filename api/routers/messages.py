from fastapi import (
    APIRouter,
    Depends,
)

from queries.messages import MessageQueries
from authenticator import authenticator
from .users import UserToken


router = APIRouter()


@router.post("/messages")
async def create_message(
    receiver_id: int,
    message_content: str,
    sender: UserToken = Depends(authenticator.get_current_account_data),
    message: MessageQueries = Depends(),
):
    sender_id = sender["id"]
    try:
        message.create_message(sender_id, receiver_id, message_content)
        return {
            "Message": " Message sent to user successfully",
        }
    except Exception as e:
        error_message = f"Error Message is {str(e)}"
        return {"error": error_message}


async def get_current_user_id(
    token: UserToken = Depends(authenticator.get_current_account_data),
):
    sender_id = token["user"]["id"]
    return sender_id
