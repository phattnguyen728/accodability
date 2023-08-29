from fastapi import APIRouter, Depends
from typing import Union, List
from queries.comments import (
    Error,
    CommentQueries,
    CommentIn,
    CommentOut,
    CommentEdit,
)
from psycopg.errors import ForeignKeyViolation
from authenticator import authenticator

router = APIRouter()


@router.get(
    "/api/posts/{post_id}/comments",
    response_model=Union[List[CommentOut], Error],
)
async def get_comments(
    post_id: int,
    repo: CommentQueries = Depends(),
    account_data: dict = Depends(authenticator.get_current_account_data),
):
    return repo.get_comments(post_id)


@router.post(
    "/api/posts/{post_id}/comments",
    response_model=Union[CommentOut, Error],
)
async def create_comment(
    post_id: int,
    comment: CommentIn,
    repo: CommentQueries = Depends(),
    account_data: dict = Depends(authenticator.get_current_account_data),
):
    return repo.create_comment(post_id, comment)


@router.delete("/api/posts/{post_id}/comments/{id}", response_model=bool)
async def delete_comment(
    post_id: int,
    id: int,
    repo: CommentQueries = Depends(),
    account_data: dict = Depends(authenticator.get_current_account_data),
):
    return repo.delete_comment(post_id, id)


@router.put(
    "/api/posts/{post_id}/comments/{id}",
    response_model=Union[CommentOut, Error],
)
async def update_comment(
    post_id: int,
    id: int,
    body: CommentEdit,
    repo: CommentQueries = Depends(),
    account_data: dict = Depends(authenticator.get_current_account_data),
):
    return repo.update_comment(post_id, id, body)


@router.get(
    "/api/users/{author_id}/comments/",
    response_model=Union[List[CommentOut], Error],
)
async def get_comments_by_user(
    author_id: int,
    repo: CommentQueries = Depends(),
    account_data: dict = Depends(authenticator.get_current_account_data),
):
    return repo.get_comments_by_user(author_id)
