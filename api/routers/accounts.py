# from fastapi import (
#     Depends,
#     HTTPException,
#     status,
#     Response,
#     APIRouter,
#     Request,
# )
# from jwtdown_fastapi.authentication import Token
# from authenticator import authenticator

# from pydantic import BaseModel

# from queries.accounts import (
#     AccountIn,
#     AccountOut,
#     AccountOutWithPassword,
#     AccountQueries,
#     DuplicateAccountError,
# )
# from typing import List, Optional, Union


# class AccountForm(BaseModel):
#     username: str
#     password: str


# class AccountToken(Token):
#     account: AccountOut


# class HttpError(BaseModel):
#     detail: str


# router = APIRouter()


# @router.post("/accounts", response_model=AccountToken | HttpError)
# async def create_account(
#     info: AccountIn,
#     request: Request,
#     response: Response,
#     account: AccountQueries = Depends(),
# ):
#     hashed_password = authenticator.hash_password(info.password)
#     try:
#         account = account.create_user(info, hashed_password)
#     except DuplicateAccountError:
#         raise HTTPException(
#             status_code=status.HTTP_400_BAD_REQUEST,
#             detail="Cannot create an account with those credentials",
#         )
#     form = AccountForm(username=info.username, password=info.password)
#     token = await authenticator.login(response, request, form, account)
#     return AccountToken(account=account, **token.dict())


# @router.get(
#     "/accounts/{username_email_or_id}", response_model=Optional[AccountOut]
# )
# def get_user_by_username_email_or_id(
#     username_email_or_id: str,
#     response: Response,
#     repo: AccountQueries = Depends(),
# ) -> Optional[AccountOut]:
#     if username_email_or_id.isdigit():
#         account = repo.get_user_by_id(int(username_email_or_id))
#     else:
#         account = repo.get_user(username_email_or_id)
#     if username_email_or_id is None:
#         response.status_code == 400
#     return account

#     # if username_email_or_id is None:
#     # response_model= Union[AccountOut, Error]
#     #

from fastapi import (
    APIRouter,
    Depends,
    Response,
    Request,
    status,
    HTTPException,
)
from typing import List, Optional
from queries.accounts import (
    DuplicateAccountError,
    AccountIn,
    AccountOut,
    AccountQueries,
    AccountOutWithPassword,
)
from jwtdown_fastapi.authentication import Token
from authenticator import authenticator
from pydantic import BaseModel


class AccountForm(BaseModel):
    username: str
    password: str


class AccountToken(Token):
    user: AccountOut


class HttpError(BaseModel):
    detail: str


router = APIRouter()


@router.post("/users", response_model=AccountToken | HttpError)
async def create_user(
    info: AccountIn,
    request: Request,
    response: Response,
    users: AccountQueries = Depends(),
):
    hashed_password = authenticator.hash_password(info.password)

    try:
        user = users.create_user(info, hashed_password)
    except DuplicateAccountError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Cannot create a user with those credentials",
        )
    form = AccountForm(username=info.username, password=info.password)
    token = await authenticator.login(response, request, form, users)
    return AccountToken(user=user, **token.dict())


@router.get("/token", response_model=AccountToken | None)
async def get_token(
    request: Request,
    user: AccountOutWithPassword = Depends(
        authenticator.try_get_current_account_data
    ),
) -> AccountToken | None:
    if user and authenticator.cookie_name in request.cookies:
        return {
            "access_token": request.cookies[authenticator.cookie_name],
            "type": "Bearer",
            "user": user,
        }


@router.get("/users", response_model=List[AccountOut])
def get_all_users(
    repo: AccountQueries = Depends(),
):
    return repo.get_all()


@router.get(
    "/users/{username_email_or_id}", response_model=Optional[AccountOut]
)
def get_user_by_username_email_or_id(
    username_email_or_id: str,
    response: Response,
    repo: AccountQueries = Depends(),
) -> Optional[AccountOut]:
    if username_email_or_id.isdigit():
        user = repo.get_user_by_id(int(username_email_or_id))
    else:
        user = repo.get_user(username_email_or_id)
    if user is None:
        response.status_code = 404
    return user


@router.delete("/users/{id}", response_model=bool)
def delete_user(
    id: int,
    repo: AccountQueries = Depends(),
    account_data: dict = Depends(authenticator.get_current_account_data),
):
    repo.delete_user(id)
    return True


# @router.put("/users/{id}", response_model=) FINISH THIS LATER LOOK UP WHERE GET TOKEN CAME FROM
