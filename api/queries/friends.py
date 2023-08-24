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
from queries.users import UserOut, UserQueries
from routers.users import UserToken, HttpError
from jwtdown_fastapi.authentication import Token
from authenticator import authenticator
from pydantic import BaseModel


router = APIRouter()


class FriendRequest(BaseModel):
    sender_id: int
    receiver_id: int
    status: str


class FriendQueries:
    user_id: UserQueries = Depends()
    token: UserToken = Depends(authenticator.get_current_account_data)
    friend_id: int
    status: str

    # def send_friend_request(self, token: token, friend_id: int):
    # user_id = token["user"]["id"]
    # user_id = token.user.id
    def send_friend_request(
        self,
        # sender: token,
        receiver_id: int,
        sender_id: UserToken = Depends(
            authenticator.get_current_account_data
        ),  # 1
    ):
        # user_id = user["user"]["id"]
        # user_id = user["id"]
        print(sender_id)

        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    result = db.execute(
                        """
                        INSERT INTO friends
                        (
                            sender_id, receiver_id, status
                        )
                        VALUES
                        (%s, %s, %s)
                        WHERE sender_id = ${sender_id}
                        RETURNING receiver_id;
                        """,
                        [sender_id, receiver_id, "pending"],
                    )
        except Exception as e:
            errorMessage = f"Error Message is {str(e)}"
            return {"error": errorMessage}
