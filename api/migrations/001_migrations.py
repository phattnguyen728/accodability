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
]
