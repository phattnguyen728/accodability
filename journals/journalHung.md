8/16 journal:
Goals
-Integrate user models for
-friendship list
-friend requests
create user should be working already, now need to build code to send friend request.
need to create new sql table for friend requests(I BROKE EVERYTHING HERE LOL | clear pycache files)
-content: friend_id_1, friend_id_2. foreign key relationship & returns corresponding (might not need?)
name from said id_value

    need to finalize friendslist Model data structure

- jwtdown authentication & protected endpoints

  - login, logout, content only for logged in users

  passlib 1.7.4 - password hasing library

preliminary jwtdown-fastapi code included in separate router.py file
need to modify for friends & user models
created new sql-table in migrations called friendsList

adding these files causes fastAPI docs to not work... idk
Get-ChildItem -Recurse -Filter _.pyc | ForEach-Object { Remove-Item $\_.FullName -Force }
DELETES PYCACHE FIELS
8/17
User models, endpoints, and features work. CRUD functionality now works with protected endpoints. - I worked with phat to get these going. Moving forward we're going to use phat's code
(main difference: using the 'User' convention in our code vs 'Accounts'). Makes more sense
when reading. Meat of the code looks similar with both compared to references - can now GET, POST, and DELETE tokens on backend(login, logout, get current_user token) - can now GET all users - can now POST user (create new user) - users cannot have the same username. I think that's the only constraint, need to double check. Could also be email as well. (SQL UNIQUE value). Spent a bit trying to fix my code that wasnt broken because of that. Not fun :/ - can now GET user by email, username, or id. Phat in charge of this function, 3 edge cases accounted for - can now PUT (update) user by id - can now DELETE user
Moving forward: I'm going to start building out the friendsList and friendRequest functions and implement it on the front end. Have starter code for both already. Main concerns are adding a second 'Friendship' table to our PostgreSQL migrations file. last time i did it i broke something and had to clear all the pycache files to get back to working baseline. Fingers crossed!
Get-ChildItem -Recurse -Filter _.pyc | ForEach-Object { Remove-Item $\_.FullName -Force }
\*clear pycache files. Works for windows, unsure for MAC
course of action: move the corresponding functions to routers.accounts||users.py and queries.accounts||users.py
add sql table in migrations
develop the accept/deny function

2 options for now - approve/reject method like in conference go - status method i used in car project with tuples (not sure if this method works in FastAPI. It worked in django tho)
https://stackoverflow.com/questions/1117564/set-django-integerfield-by-choices-name
https://www.b-list.org/weblog/2007/nov/02/handle-choices-right-way/
keep testing from there

8/20
Totally forgot that I'm behind on going thru the videos and example code on Learn website. Need to watch all that stuff before I begin to move further ahead.
Other than that, I am now able to add a friend by their unique (user_id:int) on the backend. I'm also able to retireve a friendsList tied to a unique user_id on the backend. Now I need to add this feature on the front end. Then I can move on to messages and storing those messages by a specific friendshipId.

Course of action:
-get a working login/logout on the front end
-get a placeholder front end Home page working
-add a page on the front end for seeing your list of friends. - add feature to add friends with a search bar (check cars project for stateUpdate search bar)
-click button to send friend request

have two buttons to either accept or ignore friend request
-stretch goal: use pollers & rabbitMQ to send out email notification whenever one receives a friend request.

Goal after this: implement messaging feature between friends!

Get-ChildItem -Recurse -Filter “pycache” | Remove-Item -Recurse -Force
CLEARS PYCACHE FOLDERS ON WINDOWS^^^^
8/16 journal:
Goals
-Integrate user models for
-friendship list
-friend requests
create user should be working already, now need to build code to send friend request.
need to create new sql table for friend requests(I BROKE EVERYTHING HERE LOL | clear pycache files)
-content: friend_id_1, friend_id_2. foreign key relationship & returns corresponding (might not need?)
name from said id_value

    need to finalize friendslist Model data structure

- jwtdown authentication & protected endpoints

  - login, logout, content only for logged in users

  passlib 1.7.4 - password hasing library

preliminary jwtdown-fastapi code included in separate router.py file
need to modify for friends & user models
created new sql-table in migrations called friendsList

adding these files causes fastAPI docs to not work... idk
Get-ChildItem -Recurse -Filter _.pyc | ForEach-Object { Remove-Item $\_.FullName -Force }
DELETES PYCACHE FIELS
8/17
User models, endpoints, and features work. CRUD functionality now works with protected endpoints. - I worked with phat to get these going. Moving forward we're going to use phat's code
(main difference: using the 'User' convention in our code vs 'Accounts'). Makes more sense
when reading. Meat of the code looks similar with both compared to references - can now GET, POST, and DELETE tokens on backend(login, logout, get current_user token) - can now GET all users - can now POST user (create new user) - users cannot have the same username. I think that's the only constraint, need to double check. Could also be email as well. (SQL UNIQUE value). Spent a bit trying to fix my code that wasnt broken because of that. Not fun :/ - can now GET user by email, username, or id. Phat in charge of this function, 3 edge cases accounted for - can now PUT (update) user by id - can now DELETE user
Moving forward: I'm going to start building out the friendsList and friendRequest functions and implement it on the front end. Have starter code for both already. Main concerns are adding a second 'Friendship' table to our PostgreSQL migrations file. last time i did it i broke something and had to clear all the pycache files to get back to working baseline. Fingers crossed!
Get-ChildItem -Recurse -Filter _.pyc | ForEach-Object { Remove-Item $\_.FullName -Force }
\*clear pycache files. Works for windows, unsure for MAC
course of action: move the corresponding functions to routers.accounts||users.py and queries.accounts||users.py
add sql table in migrations
develop the accept/deny function

2 options for now - approve/reject method like in conference go - status method i used in car project with tuples (not sure if this method works in FastAPI. It worked in django tho)
https://stackoverflow.com/questions/1117564/set-django-integerfield-by-choices-name
https://www.b-list.org/weblog/2007/nov/02/handle-choices-right-way/
keep testing from there

8/20
Totally forgot that I'm behind on going thru the videos and example code on Learn website. Need to watch all that stuff before I begin to move further ahead.
Other than that, I am now able to add a friend by their unique (user_id:int) on the backend. I'm also able to retireve a friendsList tied to a unique user_id on the backend. Now I need to add this feature on the front end. Then I can move on to messages and storing those messages by a specific friendshipId.

Course of action:
-get a working login/logout on the front end
-get a placeholder front end Home page working
-add a page on the front end for seeing your list of friends. - add feature to add friends with a search bar (check cars project for stateUpdate search bar)
-click button to send friend request

have two buttons to either accept or ignore friend request
-stretch goal: use pollers & rabbitMQ to send out email notification whenever one receives a friend request.

Goal after this: implement messaging feature between friends!
8/22
Today I tried refactoring the friends/follow code to automatically populate the generated friends list id's to go into the sql tables. Currently have a blocker here
Have the general code up i just need to figure out how to refactor it with the correct syntax to utilize the SQL migrations table, currently trying to base it off of create_user POST request's format.
I have also moved the friends' code over into a separate file.
Tomorrow I will work on the login/logout front end auth since the backend endpoints work already. Will be based off the w15d2 Learn exploration
course of action:
create new app.js file, make the login/logout forms, verify authentication requirements.
8/23:
Sending a post request to create a friend request is working now. Next up is working building a get request that returns with a list of all one's friends. I spent 2 hours using print statements to see what data was being entered and returning. But it works now and I got a 200 status.
Friends table was modified, as well as everything in the friends.py file(s) in routers & queries. Spent a few hours tonight but it was worth it.
Course of action:
Build feature to get list of friends from tables.
Build front end Home, Login, Logout, Sign up pages.
