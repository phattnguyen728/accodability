8/16 journal:
Goals
-Integrate user models for
-friendship list
-friend requests
create user should be working already, now need to build code to send friend request.
need to create new sql table for friend requests
-content: friend_id_1, friend_id_2. foreign key relationship & returns corresponding
name from said id_value

        need to finalize friendslist Model data structure

    - jwtdown authentication & protected endpoints
        - login, logout, content only for logged in users

        passlib 1.7.4 - password hasing library

    preliminary jwtdown-fastapi code included in separate router.py file
        need to modify for friends & user models
    created new sql-table in migrations called friendsList

adding these files causes fastAPI docs to not work... idk
