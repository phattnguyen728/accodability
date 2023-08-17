# # router.py most of this is from jwtdown-fastapi, accounts changed to user
# from typing import Optional
# from api.authenticator import authenticator
# from fastapi import (
#     Depends,
#     HTTPException,
#     status,
#     Response,
#     APIRouter,
#     Request,
# )
# from jwtdown_fastapi.authentication import Token
# from .auth import authenticator
# from pydantic import BaseModel


# from queries.users import (
#     UserIn,
#     UserOut,
#     UserRepo,
#     DuplicateUserError,
# )


# class UserForm(BaseModel):
#     username: str
#     password: str


# class UserToken(Token):
#     user: UserOut


# class HttpError(BaseModel):
#     detail: str


# router = APIRouter()


# # find correct filepath
# @router.get("/api/things")
# async def get_user_data(
#     user_data: Optional[dict] = Depends(
#         authenticator.try_get_current_account_data
#     ),
# ):
#     if user_data:
#         return personalized_list
#     return general_list


# class AccountToken(Token):
#     account: AccountOut


# @router.get("/token", response_model=AccountToken | None)
# async def get_token(
#     request: Request,
#     account: Account = Depends(authenticator.try_get_current_account_data),
# ) -> AccountToken | None:
#     if account and authenticator.cookie_name in request.cookies:
#         return {
#             "access_token": request.cookies[authenticator.cookie_name],
#             "type": "Bearer",
#             "account": account,
#         }


# @router.post("/api/accounts", response_model=AccountToken | HttpError)
# async def create_account(
#     info: AccountIn,
#     request: Request,
#     response: Response,
#     repo: AccountRepo = Depends(),
# ):
#     hashed_password = authenticator.hash_password(info.password)
#     try:
#         account = repo.create(info, hashed_password)
#     except DuplicateAccountError:
#         raise HTTPException(
#             status_code=status.HTTP_400_BAD_REQUEST,
#             detail="Cannot create an account with those credentials",
#         )
#     form = AccountForm(username=info.email, password=info.password)
#     token = await authenticator.login(response, request, form, repo)
#     return AccountToken(account=account, **token.dict())
