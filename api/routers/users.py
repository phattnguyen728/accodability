from fastapi import (
    APIRouter,
    Depends,
    Response,
    Request,
    status,
    HTTPException,
)
from typing import List, Optional
from queries.users import (
    DuplicateUserError,
    UserIn,
    UserOut,
    UserQueries,
    UserUpdate,
    UserOutWithPassword,
    Friendship,
)
from jwtdown_fastapi.authentication import Token
from authenticator import authenticator
from pydantic import BaseModel


class UserForm(BaseModel):
    username: str
    password: str


class UserToken(Token):
    user: UserOut


class HttpError(BaseModel):
    detail: str


router = APIRouter()

users = []
friendships = []


@router.post("/followers")
def follow_user(friendship: Friendship):
    friendships.append(friendship)
    return friendship


@router.get("/followers/{user_id}")
def get_follower_list(user_id: int):
    friends = [x.friend_id for x in friendships if x.user_id == user_id]
    return friends


@router.post("/users", response_model=UserToken | HttpError)
async def create_user(
    info: UserIn,
    request: Request,
    response: Response,
    users: UserQueries = Depends(),
):
    hashed_password = authenticator.hash_password(info.password)

    try:
        user = users.create_user(info, hashed_password)
    except DuplicateUserError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Cannot create a user with those credentials",
        )
    form = UserForm(username=info.username, password=info.password)
    token = await authenticator.login(response, request, form, users)
    return UserToken(user=user, **token.dict())


@router.get("/token", response_model=UserToken | None)
async def get_token(
    request: Request,
    user: UserOutWithPassword = Depends(
        authenticator.try_get_current_account_data
    ),
) -> UserToken | None:
    if user and authenticator.cookie_name in request.cookies:
        return {
            "access_token": request.cookies[authenticator.cookie_name],
            "type": "Bearer",
            "user": user,
        }


@router.get("/users", response_model=List[UserOut])
def get_all_users(
    repo: UserQueries = Depends(),
):
    return repo.get_all()


@router.put("/users/{id}", response_model=UserOut)
def update_user(
    id: int,
    user: UserUpdate,
    repo: UserQueries = Depends(),
    account_data: dict = Depends(authenticator.get_current_account_data),
):
    hashed_password = authenticator.hash_password(user.password)
    record = repo.update_user(id, user, hashed_password)
    return record


@router.delete("/users/{id}", response_model=bool)
def delete_user(
    id: int,
    repo: UserQueries = Depends(),
    account_data: dict = Depends(authenticator.get_current_account_data),
):
    repo.delete_user(id)
    return True


@router.get("/users/{username_email_or_id}", response_model=Optional[UserOut])
def get_user_by_username_email_or_id(
    username_email_or_id: str,
    response: Response,
    repo: UserQueries = Depends(),
) -> Optional[UserOut]:
    if username_email_or_id.isdigit():
        user = repo.get_user_by_id(int(username_email_or_id))
    else:
        user = repo.get_user(username_email_or_id)
    if user is None:
        response.status_code = 400
    return user
