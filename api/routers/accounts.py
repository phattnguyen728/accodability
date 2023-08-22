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
    AccountUpdate,
    Friendship,
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


# class Friendship(BaseModel):
#     user_id: int
#     friend_id: int

#     # # are_they_friends: bool
#     # @app.get("/friendships")
#     # def create_friendships(friendship: Friendship):
#     #     friendships.append(friendship)
#     #     return friendship

#     # @app.get("/friendships/{user_id}")
#     # def get_friendsList(user_id: int):
#     #     friends = [x.friend_id for x in friendships if x.user_id == user_id]
#     #     return friends
#     # def add_friend(
#     #         self, user_id: AccountOut
#     # ) ->
router = APIRouter()

users = []
friendships = []


@router.post("/friendships")
def create_friendships(friendship: Friendship):
    friendships.append(friendship)
    return friendship


@router.get("/friendships/{user_id}")
def get_friendsList(user_id: int):
    friends = [x.friend_id for x in friendships if x.user_id == user_id]
    return friends


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


# determine user token origin
@router.put("/users/{id}", response_model=AccountOut)
def update_user(
    id: int,
    user: AccountUpdate,
    repo: AccountQueries = Depends(),
    account_data: dict = Depends(authenticator.get_current_account_data),
):
    hashed_password = authenticator.hash_password(user.password)
    record = repo.update_user(id, user, hashed_password)
    return record
