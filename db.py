# database.py

import sqlite3


def create_table():
    conn = sqlite3.connect(":memory:")  # Используем in-memory базу
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)")
    cursor.execute("INSERT INTO users (name) VALUES ('Alice'), ('Bob')")
    conn.commit()
    return conn


def vulnerable_query(conn, user_input):
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE name = '{user_input}'"
    cursor.execute(query)
    return cursor.fetchall()


def safe_query(conn, user_input):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE name = ?", (user_input,))
    return cursor.fetchall()