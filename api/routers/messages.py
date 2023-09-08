from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
)

from queries.messages import MessageQueries, MessageIn
from authenticator import authenticator
from .users import UserToken


router = APIRouter()


@router.post("/messages")
async def create_message(
    message_form: MessageIn,
    sender: UserToken = Depends(authenticator.get_current_account_data),
    message: MessageQueries = Depends(),
):
    if message_form.sender_id is None:
        sender_id = sender["id"]
    else:
        sender_id = message_form.sender_id

    receiver_id = message_form.receiver_id
    message_content = message_form.message_content

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


@router.get("/messages")
async def get_message_inbox(
    user: UserToken = Depends(authenticator.get_current_account_data),
    messages: MessageQueries = Depends(),
):
    user_id = user["id"]
    try:
        if user is None:
            raise HTTPException(
                status_code=401, detail="User information not found in token"
            )
        message_inbox = messages.get_message_inbox(user_id)
        return {"Message Inbox": message_inbox}
    except Exception as e:
        error_message = f"Error Message is {str(e)}"
        return {"error": error_message}
