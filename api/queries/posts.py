from datetime import datetime
from queries.pool import pool
from typing import List, Optional
from pydantic import BaseModel


class Error(BaseModel):
    message: str


class PostIn(BaseModel):
    title: str
    body: str
    hyperlink: Optional[str]
    author_id: int


class PostOut(BaseModel):
    id: int
    title: str
    body: str
    hyperlink: Optional[str]
    author_id: int
    created_at: datetime


class PostListOut(BaseModel):
    posts: list[PostOut]


class PostQueries:
    def get_all(self) -> List[PostOut]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as cur:
                    cur.execute("""SELECT * FROM posts""")
                    return [
                        PostOut(
                            id=record[0],
                            title=record[1],
                            body=record[2],
                            hyperlink=record[3],
                            author_id=record[4],
                            created_at=record[5]
                        )
                        for record in cur
                    ]
        except Exception as e:
            print(e)
            return {"message": "Could not retrieve posts."}
