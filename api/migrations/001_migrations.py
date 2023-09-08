steps = [
    [
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
        """
        DROP TABLE (users, friendsList);
        """,
    ],
    [
        """
        CREATE TABLE posts (
            id SERIAL PRIMARY KEY NOT NULL,
            title VARCHAR(150) NOT NULL,
            body TEXT NOT NULL,
            hyperlink VARCHAR(400),
            author_id INT NOT NULL REFERENCES users(id),
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL
        );
        """,
        """
        DROP TABLE posts;
        """,
    ],
    [
        """
        CREATE TABLE comments (
            id SERIAL PRIMARY KEY NOT NULL,
            author_id INT NOT NULL REFERENCES users(id),
            post_id INT NOT NULL REFERENCES posts(id),
            body TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL
        );
        """,
        """
        DROP TABLE comments;
        """,
    ],
    [
        """
        CREATE TABLE friends(
        id serial PRIMARY KEY NOT NULL,
        sender_id INTEGER REFERENCES users(id),
        receiver_id INTEGER REFERENCES users(id),
        status varchar(50) DEFAULT 'pending',
        CONSTRAINT unique_user_friend UNIQUE (sender_id, receiver_id)

        );
        """,
        """
        DROP TABLE friends;
        """,
    ],
    [
        """
        CREATE TABLE messages(
        id serial PRIMARY KEY NOT NULL,
        sender_id INTEGER REFERENCES users(id),
        receiver_id INTEGER REFERENCES users(id),
        message_content TEXT NOT NULL
        );
        """,
        """
        DROP TABLE messages;
        """,
    ],
]
