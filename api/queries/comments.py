from datetime import datetime
from queries.pool import pool
from typing import List, Union
from pydantic import BaseModel


class Error(BaseModel):
    message: str


class CommentEdit(BaseModel):
    body: str


class CommentIn(BaseModel):
    author_id: int
    body: str


class CommentOut(BaseModel):
    id: int
    author_id: int
    post_id: int
    body: str
    created_at: datetime


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
            return Error(
                {"message": f"Could not retrieve comments due to: {e}"}
            )

    def create_comment(
        self, post_id: int, comment: CommentIn
    ) -> Union[CommentOut, Error]:
        try:
            ValueError
            with pool.connection() as conn:
                with conn.cursor() as cur:
                    result = cur.execute(
                        """
                        INSERT INTO comments
                            (author_id, post_id, body)
                        VALUES
                            (%s, %s, %s)
                        RETURNING id, created_at;
                        """,
                        [comment.author_id, post_id, comment.body],
                    )
                    data = result.fetchone()
                    id = data[0]
                    created_at = data[1]
                    old_data = comment.dict()
                    return CommentOut(
                        id=id,
                        post_id=post_id,
                        **old_data,
                        created_at=created_at,
                    )
        except Exception as e:
            return Error(
                {"message": f"Could not create a comment due to: {e}"}
            )

    def delete_comment(self, post_id: int, id: int) -> bool:
        try:
            with pool.connection() as conn:
                with conn.cursor() as cur:
                    cur.execute(
                        """
                        DELETE FROM comments
                        WHERE post_id = %s AND id = %s
                        """,
                        [post_id, id],
                    )
                    return True
        except Exception as e:
            return Error(
                {"message": f"Could not delete specified comment due to: {e}"}
            )

    def update_comment(
        self, post_id: int, id: int, body: CommentEdit
    ) -> Union[CommentOut, Error]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as cur:
                    cur.execute(
                        """
                        UPDATE comments
                        SET body = %s, created_at = %s
                        WHERE post_id = %s AND id = %s
                        """,
                        [body.body, datetime.now(), post_id, id],
                    )
                    result = cur.execute(
                        """
                        SELECT * FROM comments
                        WHERE id = %s
                        """,
                        [id],
                    )
                    data = result.fetchone()
                    print(data)
                    author_id = data[1]
                    created_at = data[4]
                    return CommentOut(
                        id=id,
                        author_id=author_id,
                        post_id=post_id,
                        body=body.body,
                        created_at=created_at,
                    )
        except Exception as e:
            return Error(
                {"message": f"Could not delete specified comment due to: {e}"}
            )

    def get_comments_by_user(self, author_id: int) -> Union[CommentOut, Error]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as cur:
                    cur.execute(
                        """
                        SELECT id, author_id, post_id, body, created_at
                        FROM comments
                        WHERE author_id = %s
                        ORDER BY created_at DESC
                        """,
                        [author_id],
                    )
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
            return Error(
                {"message": f"Could not retrieve comments due to: {e}"}
            )
