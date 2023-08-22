from pydantic import BaseModel
from typing import List, Optional
from queries.pool import pool


class DuplicateUserError(ValueError):
    message: str


class UserIn(BaseModel):
    first_name: str
    last_name: str
    username: str
    password: str
    email: str


class UserUpdate(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    username: Optional[str]
    password: Optional[str]
    email: Optional[str]


class UserOut(BaseModel):
    id: str
    first_name: str
    last_name: str
    username: str
    email: str


class UserOutWithPassword(UserOut):
    hashed_password: str


class UserQueries:
    def create_user(
        self, user: UserIn, hashed_password: str
    ) -> UserOutWithPassword:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    result = db.execute(
                        """
                        INSERT INTO users
                            (
                                first_name,
                                last_name,
                                username,
                                hashed_password,
                                email
                            )
                        VALUES
                            (%s, %s, %s, %s, %s)
                        RETURNING id;
                        """,
                        [
                            user.first_name,
                            user.last_name,
                            user.username,
                            hashed_password,
                            user.email,
                        ],
                    )
                    id = result.fetchone()[0]
                    data = user.dict()
                    return UserOutWithPassword(
                        id=id, **data, hashed_password=hashed_password
                    )
        except Exception:
            return {"Error": "Could not create User"}

    def get_user(self, username_email: str) -> UserOutWithPassword:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    result = db.execute(
                        """
                        SELECT
                            id,
                            first_name,
                            last_name,
                            username,
                            hashed_password,
                            email
                        FROM users
                        WHERE username = %s
                        or email = %s
                        """,
                        [username_email, username_email],
                    )
                    user = result.fetchone()
                    if user is None:
                        return None
                    return UserOutWithPassword(
                        id=user[0],
                        first_name=user[1],
                        last_name=user[2],
                        username=user[3],
                        hashed_password=user[4],
                        email=user[5],
                    )
        except Exception:
            return {"Error": "Could not get user by username or email"}

    def get_user_by_id(self, user_id: int) -> UserOutWithPassword:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    result = db.execute(
                        """
                        Select
                            id,
                            first_name,
                            last_name,
                            username,
                            hashed_password,
                            email
                        FROM users
                        WHERE id = %s
                        """,
                        [user_id],
                    )
                    user = result.fetchone()
                    if user is None:
                        return None
                    return UserOutWithPassword(
                        id=user[0],
                        first_name=user[1],
                        last_name=user[2],
                        username=user[3],
                        hashed_password=user[4],
                        email=user[5],
                    )
        except Exception:
            return {"Error": "Could not get user by id"}

    def get_all(self) -> List[UserOutWithPassword]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    result = db.execute(
                        """
                        SELECT
                            id,
                            first_name,
                            last_name,
                            username,
                            hashed_password,
                            email
                        FROM users
                        ORDER BY id;
                        """
                    )
                    result = []
                    for user in db:
                        user = UserOutWithPassword(
                            id=user[0],
                            first_name=user[1],
                            last_name=user[2],
                            username=user[3],
                            hashed_password=user[4],
                            email=user[5],
                        )
                        result.append(user)
                    return result
        except Exception:
            return {"Error": "Could not get all Users"}

    def update_user(
        self, user_id: int, user: UserUpdate, hashed_password: str
    ) -> UserOutWithPassword:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    db.execute(
                        """
                        UPDATE users
                        SET first_name = %s,
                        last_name = %s,
                        username = %s,
                        hashed_password = %s,
                        email = %s
                        WHERE id = %s;
                        """,
                        [
                            user.first_name,
                            user.last_name,
                            user.username,
                            hashed_password,
                            user.email,
                            user_id,
                        ],
                    )
                    data = user.dict()
                    return UserOutWithPassword(
                        id=user_id, **data, hashed_password=hashed_password
                    )
        except Exception:
            return {"Error": "Could not update User"}

    def delete_user(self, user_id: int) -> bool:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    db.execute(
                        """
                        DELETE FROM users
                        WHERE id = %s
                        """,
                        [user_id],
                    )
        except Exception as e:
            print(e)
            return {"Error": "Could not delete User"}
