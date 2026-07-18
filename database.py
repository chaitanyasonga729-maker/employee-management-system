import sqlite3

DATABASE_NAME = "database/employee.db"


def create_connection():
    return sqlite3.connect(DATABASE_NAME)


def create_tables():
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
        username TEXT PRIMARY KEY,
        password TEXT NOT NULL
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS employees(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER,
        gender TEXT,
        email TEXT,
        phone TEXT,
        department TEXT,
        designation TEXT,
        salary REAL,
        joining_date TEXT
    )
    """)

    conn.commit()
    conn.close()