from fastapi import (
    APIRouter,
    Depends,
    Response,
    Request,
    status,
    HTTPException,
)
from typing import List, Optional, Literal, Union
from queries.pool import pool
from queries.users import UserOut, UserQueries
from routers.users import UserToken, HttpError
from jwtdown_fastapi.authentication import Token
from authenticator import authenticator
from pydantic import BaseModel


router = APIRouter()


class Error(BaseModel):
    message: str


class FriendRequestIn(BaseModel):
    sender_id: int
    receiver_id: int
    status: str


class FriendRequestOut(BaseModel):
    id: int
    sender_id: int
    receiver_id: int
    # status: str


class FriendListOut(BaseModel):
    sender_id: list[FriendRequestOut]


class FriendQueries:
    def send_friend_request(
        self, sender_id, receiver_id
    ) -> Union[List[FriendListOut], Error]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as cur:
                    cur.execute(
                        """
                        INSERT INTO FRIENDS (sender_id, receiver_id)
                        VALUES (%s, %s) 
                        """,
                        [sender_id, receiver_id],
                    )
        except Exception as e:
            print(e)
            return {"message": "Could not send friend request"}

    def get_pending_friend_requests(
        self, user_id
    ) -> Union[List[FriendListOut], Error]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as cur:
                    cur.execute(
                        """
                        SELECT sender_id
                        FROM friends
                        WHERE receiver_id = %s 
                        """,
                        [user_id],
                    )
                    return cur.fetchall()
        except Exception as e:
            errorMessage = f"Error Message is {str(e)}"
            return {"error": errorMessage}, print(errorMessage)
