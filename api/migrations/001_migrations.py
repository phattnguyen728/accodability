steps = [
    [
        # "Up" SQL statement
        """
        CREATE TABLE users (
          id SERIAL PRIMARY KEY NOT NULL,
          first_name VARCHAR(50) NOT NULL,
          last_name VARCHAR(50) NOT NULL,
          username VARCHAR(50) NOT NULL UNIQUE,
          hashed_password VARCHAR(100) NOT NULL,
          email VARCHAR(100) NOT NULL UNIQUE

        );
        CREATE TABLE friendsList(
        id serial PRIMARY KEY NOT NULL,
        user_id INTEGER REFERENCES users(id),
        friend_id INTEGER REFERENCES users(id),
        CONSTRAINT unique_user_friend UNIQUE (user_id, friend_id)

        )

        """,
        # "Down" SQL statement
        """
        DROP TABLE users;
        """,
    ],
]


# check friendsList table for functionality
# DROP TABLE users, friendsList;
