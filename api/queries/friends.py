from fastapi import (
    APIRouter,
)
from typing import List, Union
from queries.pool import pool
from pydantic import BaseModel


router = APIRouter()


class Error(BaseModel):
    message: str


class FriendRequestIn(BaseModel):
    sender_id: int
    receiver_id: int


class FriendRequestApprove(BaseModel):
    sender_id: int
    receiver_id: int


class FriendRequestOut(BaseModel):
    id: int
    sender_id: int
    receiver_id: int
    status: str


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
    ) -> Union[List[FriendRequestOut], Error]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as cur:
                    cur.execute(
                        """
                        SELECT id, sender_id, receiver_id, status
                        FROM friends
                        WHERE receiver_id = %s
                        """,
                        [user_id],
                    )
                    friends = []
                    for row in cur:
                        message = FriendRequestOut(
                            id=row[0],
                            sender_id=row[1],
                            receiver_id=row[2],
                            status=row[3],
                        )
                        friends.append(message)
                    return friends

        except Exception as e:
            errorMessage = f"Error Message is {str(e)}"
            return {"error": errorMessage}, print(errorMessage)

    def approve_friend_request(
        self, sender_id, receiver_id
    ) -> Union[List[FriendRequestOut], Error]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as cur:
                    approved = "approved"
                    cur.execute(
                        """
                        UPDATE friends
                        SET status = %s
                        WHERE receiver_id = %s AND sender_id = %s
                        """,
                        [approved, receiver_id, sender_id],
                    )
                    if cur.rowcount == 1:
                        result = cur.execute(
                            """
                            SELECT * FROM friends
                            WHERE receiver_id = %s
                            """,
                            [receiver_id],
                        )
                    approved = result.fetchone()
                    if approved:
                        return FriendRequestOut(
                            id=approved[0],
                            sender_id=approved[1],
                            receiver_id=approved[2],
                            status=approved[3],
                        )
                    return None

        except Exception as e:
            errorMessage = f"Error Message is {str(e)}"
            return {"error": errorMessage}, print(errorMessage)
