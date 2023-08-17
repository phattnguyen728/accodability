import os
from psycopg_pool import ConnectionPool
from typing import List, Literal
from pydantic import BaseModel

pool = ConnectionPool(conninfo=os.environ["DATABASE_URL"])


class DuplicateAccountError(ValueError):
    pass


class AccountOut(BaseModel):
    id: int
    first: str
    last: str
    avatar: str
    email: str
    username: str


class AccountListOut(BaseModel):
    users: list[AccountOut]


class AccountIn(BaseModel):
    first: str
    last: str
    avatar: str
    email: str
    username: str
    password: str


class AccountOutWithPassword(AccountOut):
    hashed_password: str


class AccountQueries:
    def get_all_users(self) -> List[AccountOut]:
        with pool.connection() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    SELECT id, first, last, avatar,
                        email, username
                    FROM users
                    ORDER BY last, first
                """
                )

                results = []
                for row in cur.fetchall():
                    record = {}
                    for i, column in enumerate(cur.description):
                        record[column.name] = row[i]
                    results.append(AccountOut(**record))

                return results

    def get_user(self, id) -> AccountOut:
        with pool.connection() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    SELECT id, first, last, avatar,
                        email, username
                    FROM users
                    WHERE id = %s
                """,
                    [id],
                )

                record = None
                row = cur.fetchone()
                if row is not None:
                    record = {}
                    for i, column in enumerate(cur.description):
                        record[column.name] = row[i]

                return AccountOut(**record)

    def create_user(
        self, data: AccountIn, hashed_password: str
    ) -> AccountOutWithPassword:
        with pool.connection() as conn:
            with conn.cursor() as cur:
                params = [
                    data.first,
                    data.last,
                    data.avatar,
                    data.email,
                    data.username,
                    data.password
                    # data.hashed_password,
                ]
                cur.execute(
                    """
                    INSERT INTO users (first, last, avatar, email, username, password)
                    VALUES (%s, %s, %s, %s, %s, %s, %s)
                    RETURNING id, first, last, avatar, email, username
                    """,
                    params,
                )

                record = None
                row = cur.fetchone()
                if row is not None:
                    record = {}
                    for i, column in enumerate(cur.description):
                        record[column.name] = row[i]

                return AccountOutWithPassword(**record)

    def delete_user(self, user_id) -> None:
        with pool.connection() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    DELETE FROM users
                    WHERE id = %s
                    """,
                    [user_id],
                )
