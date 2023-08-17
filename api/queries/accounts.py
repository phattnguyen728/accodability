# from typing import List, Literal
# from pydantic import BaseModel
# from queries.pool import pool


# class DuplicateAccountError(ValueError):
#     pass


# class AccountOut(BaseModel):
#     id: str
#     first_name: str
#     last_name: str
#     username: str
#     email: str


# # class AccountListOut(BaseModel):
# #     users: list[AccountOut]


# class AccountIn(BaseModel):
#     first_name: str
#     last_name: str
#     username: str
#     password: str
#     email: str


# class AccountOutWithPassword(AccountOut):
#     hashed_password: str


# class Error(BaseModel):
#     {"error": "error message here"}


# class AccountQueries:
#     def get_all_users(self) -> List[AccountOutWithPassword]:
#         try:
#             with pool.connection() as conn:
#                 with conn.cursor() as cur:
#                     cur.execute(
#                         """
#                         SELECT
#                         id,
#                         first_name,
#                         last_name,
#                         username,
#                         hashed_password,
#                         email

#                         FROM users
#                         ORDER BY id;
#                     """
#                     )

#                     results = []
#                     for account in cur:
#                         account = AccountOutWithPassword(
#                             id=account[0],
#                             first_name=account[1],
#                             last_name=account[2],
#                             username=account[3],
#                             hashed_password=account[4],
#                             email=account[5],
#                         )
#                         results.append(account)
#                     return results
#         except Exception:
#             return {"error": "could not get all users"}

#             # results = []
#             # for row in cur.fetchall():
#             #     record = {}
#             #     for i, column in enumerate(cur.description):
#             #         record[column.name] = row[i]
#             #     results.append(AccountOut(**record))

#             # return results

#     def get_user(self, username_email: str) -> AccountOutWithPassword:
#         try:
#             with pool.connection() as conn:
#                 with conn.cursor() as cur:
#                     result = []
#                     cur.execute(
#                         """
#                         SELECT id,
#                         first_name,
#                         last_name,
#                         username,
#                         hashed_password,
#                         email
#                         FROM users
#                         WHERE username = %s
#                         or email - %s
#                         """,
#                         [username_email, username_email],
#                     )

#                     account = result.fetchone()
#                     if account is None:
#                         return None
#                     return AccountOutWithPassword(
#                         id=account[0],
#                         first_name=account[1],
#                         last_name=account[2],
#                         username=account[3],
#                         hashed_password=account[4],
#                         email=account[5],
#                     )
#         except Exception:
#             return {"error": "could not get user"}

#     def get_user_by_id(self, account_id: int) -> AccountOutWithPassword:
#         try:
#             with pool.connection() as conn:
#                 with conn.cursor() as cur:
#                     result = []
#                     cur.execute(
#                         """
#                         SELECT id,
#                         first_name,
#                         last_name,
#                         username,
#                         hashed_password,
#                         email
#                         FROM users
#                         WHERE id = %s
#                         """,
#                         [account_id],
#                     )

#                     account = result.fetchone()
#                     if account is None:
#                         return None
#                     return AccountOutWithPassword(
#                         id=account[0],
#                         first_name=account[1],
#                         last_name=account[2],
#                         username=account[3],
#                         hashed_password=account[4],
#                         email=account[5],
#                     )
#         except Exception:
#             return {"error": "could not get user"}
#             # record = None
#             # row = cur.fetchone()
#             # if row is not None:
#             #     record = {}
#             #     for i, column in enumerate(cur.description):
#             #         record[column.name] = row[i]

#             # return AccountOut(**record)

#     def create_user(
#         self, account: AccountIn, hashed_password: str
#     ) -> AccountOutWithPassword:
#         try:
#             with pool.connection() as conn:
#                 with conn.cursor() as cur:
#                     # result = [
#                     #     account.first_name,
#                     #     account.last_name,
#                     #     account.email,
#                     #     account.username,
#                     #     account.password
#                     #     # account.hashed_password,
#                     # ]
#                     result = cur.execute(
#                         """
#                         INSERT INTO users (
#                             first_name,
#                             last_name,
#                             username,
#                             hashed_password,
#                             email
#                             )
#                         VALUES (%s, %s, %s, %s, %s)
#                         RETURNING id;
#                         """,
#                         [
#                             account.first_name,
#                             account.last_name,
#                             account.username,
#                             hashed_password,
#                             account.email,
#                         ],
#                     )
#                     id = result.fetchone()[0]
#                     data = account.dict()
#                     return AccountOutWithPassword(
#                         id=id, **data, hashed_password=hashed_password
#                     )
#         except Exception:
#             return {"error": "could not create user"}
#             # record = None
#             # row = cur.fetchone()
#             # if row is not None:
#             #     record = {}
#             #     for i, column in enumerate(cur.description):
#             #         record[column.name] = row[i]

#             # return AccountOutWithPassword(**record)

#     def delete_user(self, user_id: int) -> bool:
#         try:
#             with pool.connection() as conn:
#                 with conn.cursor() as cur:
#                     cur.execute(
#                         """
#                         DELETE FROM users
#                         WHERE id = %s
#                         """,
#                         [user_id],
#                     )
#         except Exception:
#             return {"error": "could not delete user"}

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


class AccountOutWithPassword(AccountOut):
    hashed_password: str


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
