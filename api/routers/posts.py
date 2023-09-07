from fastapi import APIRouter, Depends, HTTPException
from queries.posts import PostQueries, PostOut, PostIn
from typing import List
from authenticator import authenticator
from .users import UserToken

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


@router.post(
    "/api/posts",
    response_model=PostOut,
)
async def create_post(
    post_data: PostIn,
    repo: PostQueries = Depends(),
    user: UserToken = Depends(authenticator.get_current_account_data),
):
    if post_data.author_id is None:
        author_id = user["id"]
    else:
        author_id = post_data.author_id

    title = post_data.title
    body = post_data.body
    hyperlink = post_data.hyperlink
    try:
        new_post = repo.create_post(title, body, hyperlink, author_id)
        return new_post
    except Exception:
        raise HTTPException(status_code=400, detail="could not create post.")


@router.delete("/api/posts/{post_id}", response_model=bool)
async def delete_post(
    post_id: int,
    repo: PostQueries = Depends(),
    user: UserToken = Depends(authenticator.get_current_account_data),
):
    try:
        deleted = repo.delete_post(post_id, user["id"])
        if deleted:
            return True
        else:
            raise HTTPException(status_code=404, detail="Post not found")
    except Exception:
        raise HTTPException(
            status_code=400, detail="You are not the author of this post."
        )


@router.get(
    "/api/posts/{post_id}",
    response_model=PostOut,
)
async def get_post_by_id(
    post_id: int,
    repo: PostQueries = Depends(),
):
    try:
        post = repo.get_post_by_id(post_id)
        if not post:
            raise HTTPException(status_code=404, detail="Post not found")

        return post
    except Exception:
        raise HTTPException(
            status_code=500,
            detail="An error occurred while fetching the post.",
        )


@router.put(
    "/api/posts/{post_id}",  # #/author_id{author_id}
    response_model=PostOut,
)
async def update_post(
    post_id: int,
    author_id: int,
    post_data: PostIn,
    repo: PostQueries = Depends(),
    user: UserToken = Depends(authenticator.get_current_account_data),
):
    try:
        updated_post = repo.update_post(post_id, post_data, user["id"])
        if not updated_post:
            raise HTTPException(status_code=404, detail="Post not found")
        return updated_post
    except Exception:
        raise HTTPException(
            status_code=500,
            detail="An error occurred while updating the post.",
        )
