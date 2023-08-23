import os
from fastapi import Depends
from jwtdown_fastapi.authentication import Authenticator
from queries.users import UserOutWithPassword, UserQueries, UserOut


class MyAuthenticator(Authenticator):
    async def get_account_data(
        self,
        username: str,
        users: UserQueries,
    ):
        return users.get_user(username)

    def get_account_getter(
        self,
        users: UserQueries = Depends(),
    ):
        return users

    def get_hashed_password(self, user: UserOutWithPassword):
        return user.hashed_password

    def get_account_data_for_cookie(self, user: UserOut):
        return user.id, UserOut(**user.dict())


authenticator = MyAuthenticator(
    os.environ["SIGNING_KEY"],
)
