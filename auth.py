from database import execute_query, fetch_one


def create_admin():
    """
    Creates a default admin account if it doesn't already exist.
    """

    admin = fetch_one(
        "SELECT * FROM users WHERE username=?",
        ("admin",)
    )

    if admin is None:

        execute_query(
            "INSERT INTO users(username, password) VALUES(?, ?)",
            ("admin", "admin123")
        )


def login(username, password):
    """
    Checks whether the username and password are correct.
    """

    user = fetch_one(
        "SELECT * FROM users WHERE username=? AND password=?",
        (username, password)
    )

    return user is not None


def change_password(username, old_password, new_password):
    """
    Changes the password after verifying the old password.
    """

    user = fetch_one(
        "SELECT * FROM users WHERE username=? AND password=?",
        (username, old_password)
    )

    if user:

        execute_query(
            "UPDATE users SET password=? WHERE username=?",
            (new_password, username)
        )

        return True

    return False