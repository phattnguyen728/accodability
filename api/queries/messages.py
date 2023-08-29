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

    def get_message_inbox(self, user_id) -> List[MessageOut]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as cur:
                    cur.execute(
                        """
                        SELECT id, sender_id, receiver_id, message_content
                        FROM messages
                        WHERE sender_id = %s OR receiver_id = %s
                        ORDER BY id;
                        """,
                        [user_id, user_id],
                    )
                    messages = []
                    for row in cur:
                        message = MessageOut(
                            id=row[0],
                            sender_id=row[1],
                            receiver_id=row[2],
                            message_content=row[3],
                        )
                        messages.append(message)
                    return messages
        except Exception as e:
            errorMessage = f"Error Message is {str(e)}"
            return {"error": errorMessage}
