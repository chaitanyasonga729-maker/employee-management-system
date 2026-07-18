import sqlite3
import os

# Create database folder if it doesn't exist
os.makedirs("database", exist_ok=True)

DATABASE = "database/employee.db"


def create_connection():
    """
    Creates and returns a SQLite database connection.
    """
    conn = sqlite3.connect(DATABASE)
    return conn


def create_tables():
    """
    Creates all required tables.
    """
    conn = create_connection()
    cursor = conn.cursor()

    # ----------------------------
    # Users Table
    # ----------------------------
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users(
            username TEXT PRIMARY KEY,
            password TEXT NOT NULL
        )
    """)

    # ----------------------------
    # Employees Table
    # ----------------------------
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS employees(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER,
            gender TEXT,
            email TEXT UNIQUE,
            phone TEXT,
            department TEXT,
            designation TEXT,
            salary REAL,
            joining_date TEXT
        )
    """)

    conn.commit()
    conn.close()


def execute_query(query, values=()):
    """
    Executes INSERT, UPDATE, DELETE queries.
    """
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute(query, values)

    conn.commit()
    conn.close()


def fetch_all(query, values=()):
    """
    Returns all rows.
    """
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute(query, values)

    data = cursor.fetchall()

    conn.close()

    return data


def fetch_one(query, values=()):
    """
    Returns a single row.
    """
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute(query, values)

    data = cursor.fetchone()

    conn.close()

    return data