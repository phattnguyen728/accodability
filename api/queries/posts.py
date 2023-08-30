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


class PostOut(BaseModel):
    id: int
    title: str
    body: str
    hyperlink: Optional[str]
    author_id: int
    created_at: datetime


class PostListOut(BaseModel):
    posts: List[PostOut]


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

    def create_post(self, post_data: PostIn, author_id: int) -> PostOut:
        try:
            with pool.connection() as conn:
                with conn.cursor() as cur:
                    result = cur.execute(
                        """
                        INSERT INTO posts (title, body, hyperlink, author_id, created_at)
                        VALUES (%s, %s, %s, %s, %s)
                        RETURNING id, author_id, created_at
                        """,
                        (
                            post_data.title,
                            post_data.body,
                            post_data.hyperlink,
                            author_id,
                            datetime.now(),
                         ),
                    )
                    data = result.fetchone()
                    new_post_id = data[0]
                    created_at = data[1]
                    return PostOut(
                        id=new_post_id,
                        title=post_data.title,
                        body=post_data.body,
                        hyperlink=post_data.hyperlink,
                        author_id=author_id,
                        created_at=created_at,
                    )
        except Exception as e:
            print(e)
            return {"message": "Could not create post"}

    # Get request to fetch specific post and load all comments
    def get_post_by_id(self, post_id: int) -> Optional[PostOut]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as cur:
                    cur.execute(
                        "SELECT * FROM posts WHERE id = %s",
                        [post_id],
                    )
                    record = cur.fetchone()
                    if record:
                        return PostOut(
                            id=record[0],
                            title=record[1],
                            body=record[2],
                            hyperlink=record[3],
                            author_id=record[4],
                            created_at=record[5],
                        )
                    return None
        except Exception as e:
            print(e)

    def delete_post(self, post_id: int, author_id: int) -> bool:
        try:
            with pool.connection() as conn:
                with conn.cursor() as cur:
                    cur.execute(
                        """DELETE FROM posts WHERE id = %s AND author_id = %s""",
                        [post_id, author_id],
                    )
                    if cur.rowcount == 1:
                        cur.execute(
                            """
                            DELETE FROM comments
                            WHERE post_id = %s
                            """,
                            [post_id],
                        )
                        return True
                    else:
                        return False
        except Exception as e:
            print(e)
            return False
    # put request still working on this code
    # def update_post(self, post_id: int, post_data: PostIn) -> Optional[PostOut]:
    #     try:
    #         with pool.connection() as conn:
    #             with conn.cursor() as cur:
    #                 cur.execute(
    #                     """
    #                     UPDATE posts
    #                     SET title = %s, body = %s, hyperlink = %s
    #                     WHERE id = %s
    #                     RETURNING id, created_at
    #                     """,
    #                     [post_data.title, post_data.body, post_data.hyperlink, post_id],
    #                 )
    #                 result = cur.execute(
    #                     """
    #                     SELECT * FROM posts
    #                     WHERE id = %s
    #                     """,
    #                     [post_id],
    #                 )
    #                 record = result.fetchone()
    #                 created_at = record[5]
    #                 return PostOut(
    #                     id=post_id,
    #                     title=post_data.title,
    #                     body=post_data.body,
    #                     hyperlink=post_data.hyperlink,
    #                     author_id=post_data.author_id,
    #                     created_at=created_at,
    #                     )
    #                 return None
    #     except Exception as e:
    #         print(e)
    #         return None
