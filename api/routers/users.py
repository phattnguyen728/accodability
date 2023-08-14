from fastapi import APIRouter, Depends, HTTPException
from queries.users import UserQueries, UserListOut, UserOut, UserIn
from psycopg.errors import UniqueViolation

# Implement the following endpoints
# 1. get a user with a specific id
# 2. get all users
# 3. create a user
# 4. delete a user
#
# Resources
# routers.trucks example
# users.queries
# docs page (at http://localhost:8000/docs#)
# Notion: https://marbled-particle-5cf.notion.site/FastAPI-2eee765c870245ab9f28a3ef5456a981?pvs=4
# take note of endpoints best practices

router = APIRouter()


@router.get("/api/users/{user_id}", response_model=UserOut)
def get_user(
    user_id: int,
    queries: UserQueries = Depends(),
):
    record = queries.get_user(user_id)
    if record is None:
        raise HTTPException(
            status_code=404, detail="No user found with id {}".format(user_id)
        )
    else:
        return record


@router.delete("/api/users/{user_id}", response_model=bool)
def delete_user(user_id: int, queries: UserQueries = Depends()):
    queries.delete_user(user_id)
    return True


@router.get("/api/users", response_model=UserListOut)
def get_users(queries: UserQueries = Depends()):
    # returning a JSON object is conventional -- preferred instead of returning
    # a list due to historical # security reasons and flexibility
    return {"users": queries.get_all_users()}


@router.post("/api/users", response_model=UserOut)
def create_user(
    user: UserIn,
    queries: UserQueries = Depends(),
):
    # It's fine if you didn't include this, but you might have run into this in testing -- if you try
    # to create a user with an already existing username or email, the server throws a 500 error
    # because of exceptions coming from create_user. We should stop it from being a 500 and inform
    # the client of more specific details.

    try:
        return queries.create_user(user)
    except UniqueViolation as e:
        raise HTTPException(status_code=400, detail=str(e))
