from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

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
create table users(
    id serial not null primary key,
    name varchar(100) not null,
    username varchar(100) not null unique,
)

create table friendsList(
    id serial not null primary key,
    friendsList tuple not null unique,    #lookup tuple in table postgreSQL

)

@app.get("/users")
def get_users():
    return users

@app.get("/friendships")
def create_friendships(friendship: Friendship):
    friendships.append(friendship)
    return friendship

@app.get("/friendships/{user_id}")
def get_friends(user_id: int):
    friends = [x.friend_id for x in friendships if x.user_id == user_id]
    return friends
