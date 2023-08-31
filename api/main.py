from authenticator import authenticator
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import users, friends, posts, messages
from routers import comments
import os


app = FastAPI()
app.include_router(authenticator.router)
app.include_router(users.router)
app.include_router(friends.router)
app.include_router(posts.router)
app.include_router(comments.router)
app.include_router(messages.router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[os.environ.get("CORS_HOST", "http://localhost:3000")],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {"message": "You hit the root path!"}
