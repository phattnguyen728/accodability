steps = [
    [
        # "Up" SQL statement
        """
        CREATE TABLE users (
            id SERIAL PRIMARY KEY NOT NULL,
            first_name VARCHAR(50) NOT NULL,
            last_name VARCHAR(50) NOT NULL,
            username VARCHAR(100) NOT NULL UNIQUE,
            hashed_password VARCHAR(100) NOT NULL,
            email VARCHAR(100) NOT NULL UNIQUE
        );
        """,
        # "Down" SQL statement
        """
        DROP TABLE users;
        """,
    ],
    [
        """
        Create table post (
            id serial primary key not null,
            title varchar(150) not null,
            body text not null,
            hyperlink varchar(400),
            author_id INT NOT NULL REFERENCES users(id),
            created_at timestamp not null default current_timestamp
        );
        """,
        """
        DROP table post;
        """,
    ],
    [
        """
        CREATE TABLE followList(
        id serial PRIMARY KEY NOT NULL,
        user_id INTEGER REFERENCES users(id),
        friend_id INTEGER REFERENCES users(id),
        CONSTRAINT unique_user_friend UNIQUE (user_id, friend_id)

        );
        """,
        """
        DROP TABLE followList;
        """,
    ],
]
