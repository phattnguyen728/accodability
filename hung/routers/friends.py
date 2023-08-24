from fastapi import (
    APIRouter,
    Depends,
    Response,
    Request,
    status,
    HTTPException,
)
from typing import List, Optional
from queries.pool import pool
from queries.users import (
    UserOut,
)
from jwtdown_fastapi.authentication import Token
from authenticator import authenticator
from pydantic import BaseModel

users = []
friendships = []


@router.post("/followers")
async def follow_user(
    user_id: UserOut(id),
    request: Request,
    response: Response,
    users: FollowerQueries = Depends(authenticator.get_current_account_data),
):
    follow = users.create_follow(user_id, friend_id)


@router.post("/followers")
def follow_user(friendship: Friendship):
    friendships.append(friendship)
    return friendship


@router.get("/followers/{user_id}")
def get_follower_list(user_id: int):
    friends = [x.friend_id for x in friendships if x.user_id == user_id]
    return friends


# move to routers

# user_id
# zach id:1
# adam id:2
# diana id:3
# hung id:4

# followList table
# user_id: 1, friend_id: 4 (zach is following hung)
# user_id:3, friend_id:2 (diana is following adam)
# user_id 3 , friend_id 4 (diana is following hung)

# get follow list for user_id 4: it should print out column of friend ids (zach and diana)
# get a list of every
# sql SELECT to grab the friend_ids,
