from datetime import datetime
from queries.pool import pool
from typing import List, Literal, Union
from pydantic import BaseModel


class Error(BaseModel):
    message: str


class CommentIn(BaseModel):
    author_id: int
    post_id: int
    body: str


class CommentOut(BaseModel):
    id: int
    author_id: int
    post_id: int
    body: str
    created_at: datetime


class CommentListOut(BaseModel):
    comments: list[CommentOut]


class CommentQueries:
    def get_comments(self, post_id: int) -> Union[List[CommentOut], Error]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as cur:
                    cur.execute(
                        """
                        SELECT id, author_id, post_id, body, created_at
                        FROM comments
                        WHERE post_id = %s
                        ORDER BY created_at DESC
                        """,
                        [post_id],
                    )
                    print("test")
                    return [
                        CommentOut(
                            id=record[0],
                            author_id=record[1],
                            post_id=record[2],
                            body=record[3],
                            created_at=record[4],
                        )
                        for record in cur
                    ]
        except Exception as e:
            print(e)
            return {"message": "Could not retrieve comments"}
