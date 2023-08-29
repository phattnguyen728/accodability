from fastapi import APIRouter, Depends, HTTPException
from queries.posts import PostQueries, PostOut
from typing import List
from authenticator import authenticator

router = APIRouter()


@router.get(
    "/api/posts",
    response_model=List[PostOut],
)
async def get_all_posts(
    repo: PostQueries = Depends(),
    account_data: dict = Depends(authenticator.get_current_account_data),
):
    try:
        return repo.get_all()
    except Exception:
        raise HTTPException(
            status_code=400, detail="Could not retrieve posts."
        )
