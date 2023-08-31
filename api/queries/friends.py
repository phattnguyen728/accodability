from fastapi import (
    APIRouter,
)
from typing import List, Union
from queries.pool import pool
from pydantic import BaseModel

from authenticator import authenticator

router = APIRouter()


class Error(BaseModel):
    message: str


class FriendRequestIn(BaseModel):
    sender_id: int
    receiver_id: int
    username: str
    status: str


class FriendRequestOut(BaseModel):
    id: int
    sender_id: int
    receiver_id: int
    username: str
    # status: str


class FriendListOut(BaseModel):
    sender_id: list[FriendRequestOut]


class FriendQueries:
    def send_friend_request(
        self, sender_id, receiver_id, username
    ) -> Union[List[FriendListOut], Error]:
        self.username = username
        try:
            with pool.connection() as conn:
                with conn.cursor() as cur:
                    cur.execute(
                        """
                        INSERT INTO FRIENDS (sender_id, receiver_id, username)
                        VALUES (%s, %s, %s)
                        """,
                        [sender_id, receiver_id, username],
                    )
        except Exception as e:
            print(e)
            return {"message": "Could not send friend request"}

    def get_pending_friend_requests(
        self, user_id
    ) -> Union[List[FriendRequestOut], Error]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as cur:
                    cur.execute(
                        """
                        SELECT id, sender_id, receiver_id, username
                        FROM friends
                        WHERE receiver_id = %s
                        """,
                        [user_id],
                    )
                    # return cur.fetchall()
                    # friends = []
                    # message = FriendRequestOut(
                    #     id=user["id"],
                    #     sender_id=user["sender_id"],
                    #     receiver_id=user["receiver_id"],
                    #     username=user["username"],
                    # )
                    # friends.append(message)
                    # return friends
                    friends = []
                    for row in cur:
                        message = FriendRequestOut(
                            id=row[0],
                            sender_id=row[1],
                            receiver_id=row[2],
                            username=row[3],
                        )
                        friends.append(message)
                    return friends

        except Exception as e:
            errorMessage = f"Error Message is {str(e)}"
            return {"error": errorMessage}, print(errorMessage)
