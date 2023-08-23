from fastapi import APIRouter, Response, Depends
from queries.posts import PostQueries

router = APIRouter()


@router.get("/api/posts")
def get_all_posts(
    response: Response,
    blog: PostQueries = Depends(),
):
    try:
        return blog.get_all()
    except Exception:
        response.status_code = 400
        return {"message": "Could not retrieve posts."}
