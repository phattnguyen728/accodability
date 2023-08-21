from pydantic import BaseModel
from typing import List, Optional
from queries.pool import pool


class DuplicateAccountError(ValueError):
    message: str


class AccountIn(BaseModel):
    first_name: str
    last_name: str
    username: str
    password: str
    email: str


class AccountOut(BaseModel):
    id: str
    first_name: str
    last_name: str
    username: str
    email: str


class AccountUpdate(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    username: Optional[str]
    password: Optional[str]
    email: Optional[str]


class AccountOutWithPassword(AccountOut):
    hashed_password: str


class Friendship(BaseModel):
    user_id: int
    friend_id: int

    # # are_they_friends: bool
    # @app.get("/friendships")
    # def create_friendships(friendship: Friendship):
    #     friendships.append(friendship)
    #     return friendship

    # @app.get("/friendships/{user_id}")
    # def get_friendsList(user_id: int):
    #     friends = [x.friend_id for x in friendships if x.user_id == user_id]
    #     return friends
    # def add_friend(
    #         self, user_id: AccountOut
    # ) ->


class AccountQueries:
    def create_user(
        self, user: AccountIn, hashed_password: str
    ) -> AccountOutWithPassword:
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
                    return AccountOutWithPassword(
                        id=id, **data, hashed_password=hashed_password
                    )
        except Exception as e:
            print(e)
            return {"Error": "Could not create User"}

    def get_user(self, username_email: str) -> AccountOutWithPassword:
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
                    return AccountOutWithPassword(
                        id=user[0],
                        first_name=user[1],
                        last_name=user[2],
                        username=user[3],
                        hashed_password=user[4],
                        email=user[5],
                    )
        except Exception as e:
            print(e)
            return {"Error": "Could not get user by username or email"}

    def get_user_by_id(self, user_id: int) -> AccountOutWithPassword:
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
                    return AccountOutWithPassword(
                        id=user[0],
                        first_name=user[1],
                        last_name=user[2],
                        username=user[3],
                        hashed_password=user[4],
                        email=user[5],
                    )
        except Exception as e:
            print(e)
            return {"Error": "Could not get user by id"}

    def update_user(
        self, user_id: int, user: AccountUpdate, hashed_password: str
    ) -> AccountOutWithPassword:
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
                    return AccountOutWithPassword(
                        id=user_id, **data, hashed_password=hashed_password
                    )
        except Exception as e:
            print(e)
            return {"Error": "Could not update User"}

    def get_all(self) -> List[AccountOutWithPassword]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    result = db.execute(
                        """
                        SELECT id, first_name, last_name, username, hashed_password, email
                        FROM users
                        ORDER BY id;
                        """
                    )
                    result = []
                    for user in db:
                        user = AccountOutWithPassword(
                            id=user[0],
                            first_name=user[1],
                            last_name=user[2],
                            username=user[3],
                            hashed_password=user[4],
                            email=user[5],
                        )
                        result.append(user)
                    return result
        except Exception as e:
            print(e)
            return {"Error": "Could not get all Users"}

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
