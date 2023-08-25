from fastapi import APIRouter, Depends, HTTPException
from typing import Optional, Union, List
from queries.comments import Error, CommentQueries, CommentIn, CommentOut
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
