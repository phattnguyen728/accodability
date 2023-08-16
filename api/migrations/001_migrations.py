steps = [
    [
        # "Up" SQL statement
        """
        CREATE TABLE users (
          id SERIAL NOT NULL UNIQUE,
          first TEXT NOT NULL,
          last TEXT NOT NULL,
          avatar TEXT NOT NULL,
          email TEXT NOT NULL UNIQUE,
          username TEXT NOT NULL UNIQUE,
          referrer_id INTEGER REFERENCES users("id") ON DELETE CASCADE
);
        """,
        # "Down" SQL statement
        """
        DROP TABLE users;
        """,
    ],
]