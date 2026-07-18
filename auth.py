from database import create_connection


def create_admin():
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT OR IGNORE INTO users(username, password)
        VALUES(?, ?)
    """, ("admin", "admin123"))

    conn.commit()
    conn.close()


def login(username, password):
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM users
        WHERE username=? AND password=?
    """, (username, password))

    user = cursor.fetchone()

    conn.close()

    return user