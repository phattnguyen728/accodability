from typing import List, Union
from queries.pool import pool
from pydantic import BaseModel


class Error(BaseModel):
    message: str


class MessageIn(BaseModel):
    sender_id: int
    receiver_id: int
    message_content: str


class MessageOut(BaseModel):
    id: int
    sender_id: int
    receiver_id: int
    message_content: str


class MessageListOut(BaseModel):
    sender_id: list[MessageOut]


class MessageQueries:
    def create_message(
        self, sender_id, receiver_id, message_content
    ) -> Union[List[MessageListOut], Error]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as cur:
                    cur.execute(
                        """
                        INSERT INTO messages (sender_id, receiver_id, message_content)
                        VALUES (%s, %s, %s)
                        """,
                        [sender_id, receiver_id, message_content],
                    )
        except Exception as e:
            return {"message": "Could not send message to specified user"}
