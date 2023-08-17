# import os
# from fastapi import Depends
# from jwtdown_fastapi.authentication import Authenticator
# from queries.accounts import (
#     AccountQueries,
#     AccountOut,
#     AccountOutWithPassword,
# )


# class AccountAuthenticator(Authenticator):
#     async def get_account_data(
#         self,
#         username: str,
#         accounts: AccountQueries,
#     ):
#         # Use your repo to get the account based on the
#         # username (which could be an email)
#         return accounts.get_user(username)

#     def get_account_getter(
#         self,
#         accounts: AccountQueries = Depends(),
#     ):
#         # Return the accounts. That's it.
#         return accounts

#     def get_hashed_password(self, account: AccountOutWithPassword):
#         # Return the encrypted password value from your
#         # account object
#         return account.hashed_password

#     def get_account_data_for_cookie(self, account: AccountOutWithPassword):
#         # Return the username and the data for the cookie.
#         # You must return TWO values from this method.
#         return account.id, AccountOut(**account.dict())


# try:
#     signing_key = os.environ["SIGNING_KEY"]
# except KeyError:
#     print("signing key not found")
#     raise

# authenticator = AccountAuthenticator(os.environ["SIGNING_KEY"])

import os
from fastapi import Depends
from jwtdown_fastapi.authentication import Authenticator
from queries.accounts import AccountOutWithPassword, AccountQueries, AccountOut


class AccountAuthenticator(Authenticator):
    async def get_account_data(
        self,
        username: str,
        users: AccountQueries,
    ):
        return users.get_user(username)

    def get_account_getter(
        self,
        users: AccountQueries = Depends(),
    ):
        return users

    def get_hashed_password(self, user: AccountOutWithPassword):
        return user.hashed_password

    def get_account_data_for_cookie(self, user: AccountOut):
        return user.id, AccountOut(**user.dict())


try:
    signing_key = os.environ["SIGNING_KEY"]
except KeyError:
    print("signing key not found")
    raise

authenticator = AccountAuthenticator(
    os.environ["SIGNING_KEY"],
)
