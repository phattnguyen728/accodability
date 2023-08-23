steps = [
    [
        """
        Create table post (
            id serial primary key not null,
            title varchar(150) not null,
            body text not null,
            hyperlink varchar(400),
            author_id INT NOT NULL,
            created_at timestamp not null default current_timestamp
        );
        """,
        """
        DROP table post;
        """,
    ]
]
