import sqlite3
from typing import  Tuple


def create_table() -> sqlite3.Connection:
    """Создаёт временную базу данных в памяти и возвращает соединение."""
    conn = sqlite3.connect(":memory:")  # Используем in-memory базу
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)")
    cursor.execute("INSERT INTO users (name) VALUES ('Alice'), ('Bob')")
    conn.commit()
    return conn


def vulnerable_query(conn: sqlite3.Connection, user_input: str) -> list[Tuple]:
    """НЕбезопасный SQL-запрос — уязвимость SQL-инъекции."""
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE name = '{user_input}'"
    cursor.execute(query)
    return cursor.fetchall()


def safe_query(conn: sqlite3.Connection, user_input: str) -> list[Tuple]:
    """Безопасный SQL-запрос с параметризованным вводом."""
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE name = ?", (user_input,))
    return cursor.fetchall()