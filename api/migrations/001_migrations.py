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
          referrer_id INTEGER REFERENCES users(id) ON DELETE CASCADE
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
    ]
]
