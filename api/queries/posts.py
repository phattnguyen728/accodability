from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from .pool import pool


# output structure for posts
class PostOut(BaseModel):
    id: int
    title: str
    body: str
    hyperlink: Optional[str]
    created_at: datetime = datetime.now()
    author_id: int


# info required for create or update a post
class PostIn(BaseModel):
    title: str
    body: str
    hyperlink: Optional[str]
    author_id: int


class PostQueries:
    def get_all(self):
        with pool.connection() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM posts")
                return cur.fetchall(
                )
