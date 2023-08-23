from fastapi import FastAPI
from authenticator import authenticator
from routers import users
from routers import posts
import os


app = FastAPI()
app.include_router(authenticator.router)
app.include_router(users.router)
app.include_router(posts.router)
