from fastapi import (
    APIRouter,
    Depends,
    Response,
    Request,
    status,
    HTTPException,
)
from typing import List, Optional
from queries.pool import pool
from queries.users import (
    UserOut,
)
from jwtdown_fastapi.authentication import Token
from authenticator import authenticator
from pydantic import BaseModel


router = APIRouter()

users = []
friendships = []


class Friendship(BaseModel):
    user_id: int
    friend_id: int


class FollowerList:
    def create_follower_list(
        self, user: UserOut, friend_id: int
    ) -> Friendship:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    result = db.execute(
                        """INSERT INTO followList
                        (
                        user_id,
                        friend_id
                        )
                        VALUES
                        (%s, %s)
                        RETURNING friend_id;
                        """,
                        [user.id, friend_id],
                    )
        except Exception:
            return {"Error": "Could not follow this user"}


class FollowerQueries:
    def create_follow(self, user: UserOut, friend_id: int) -> Friendship:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    result = db.execute(
                        """
                        INSERT INTO followList
                        (
                            user_id,
                            friend_id
                        )
                        VALUES
                        (%s, %s)
                        RETURNING friend_id;
                        """,
                        [user.id, friend_id],
                    )
        except Exception:
            return {"Error": "Could not follow this user"}
