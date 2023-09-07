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
    username: str
    # status: str


class FriendRequestApprove(BaseModel):
    sender_id: int
    receiver_id: int
    # status: str


class FriendRequestOut(BaseModel):
    id: int
    sender_id: int
    receiver_id: int
    username: str
    status: str


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
                        SELECT id, sender_id, receiver_id, username, status
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
                            status=row[4],
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
            # with pool.connection() as conn:
            #     with conn.cursor() as cur:
            #         result = cur.execute(
            #             """
            #             SELECT receiver_id, status
            #             FROM friends
            #             WHERE receiver_id = %s
            #             """,
            #             [user_id],
            #         )
            #         data = result.fetchone()
            #         receiver_id_verify = data[0]
            # if int(receiver_id_verify) == int(receiver_id):
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
                            username=approved[3],
                            status=approved[4],
                        )
                    return None

        except Exception as e:
            errorMessage = f"Error Message is {str(e)}"
            return {"error": errorMessage}, print(errorMessage)
