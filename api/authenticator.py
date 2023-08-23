import os
from fastapi import Depends
from jwtdown_fastapi.authentication import Authenticator
<<<<<<< HEAD
from queries.accounts import AccountQueries, AccountOut, AccountOutWithPassword
=======
from queries.users import UserOutWithPassword, UserQueries, UserOut

>>>>>>> main

class MyAuthenticator(Authenticator):
    async def get_account_data(
        self,
<<<<<<< HEAD
        email: str,
        accounts: AccountQueries,
    ):
        # Use your repo to get the account based on the
        # username (which could be an email)
        return accounts.get(email)

    def get_account_getter(
        self,
        accounts: AccountQueries = Depends(),
    ):
        # Return the accounts. That's it.
        return accounts

    def get_hashed_password(self, account: AccountOutWithPassword):
        # Return the encrypted password value from your
        # account object
        return account.hashed_password

    def get_account_data_for_cookie(self, account: AccountOut):
        # Return the username and the data for the cookie.
        # You must return TWO values from this method.
        return account.email, AccountOut(**account.dict())


authenticator = MyAuthenticator(os.environ["SIGNING_KEY"])
=======
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
>>>>>>> main
