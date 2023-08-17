from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from api.authenticator import authenticator
from fastapi import APIRouter
from typing import List

app = FastAPI()
router = APIRouter()


class User(BaseModel):
    username: str
    email: str


class Friendship(BaseModel):
    user_id: int
    friend_id: int

    # are_they_friends: bool


users = []
friendships = []
# pull this from the postgres database tables
# sql setup here:
"""
create table users(
    id serial not null primary key,
    name varchar(100) not null,
    username varchar(100) not null unique,
)

create table friendsList(
    id serial not null primary key,
    friendsList tuple not null unique,    #lookup tuple in table postgreSQL

)
"""

@app.post("/login")
async def login():



@app.get("/users")
def get_users():
    return users


@app.get("/friendships")
def create_friendships(friendship: Friendship):
    friendships.append(friendship)
    return friendship


@app.get("/friendships/{user_id}")
def get_friendsList(user_id: int):
    friends = [x.friend_id for x in friendships if x.user_id == user_id]
    return friends


# @router.post("/api/things")
# async def list_friends(
#     account_data: dict = Depends(authenticator.get_current_account_data),
# ):
#     pass
