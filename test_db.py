# test_database.py

import pytest
import sqlite3
from db import create_table, vulnerable_query, safe_query


def test_vulnerable_query_valid_input():
    conn = create_table()
    result = vulnerable_query(conn, "Alice")
    assert len(result) == 1
    assert result[0][1] == "Alice"


def test_vulnerable_query_sql_injection():
    conn = create_table()
    malicious_input = "Alice'; DROP TABLE users; --"
    with pytest.raises(sqlite3.OperationalError):
        vulnerable_query(conn, malicious_input)


def test_safe_query_valid_input():
    conn = create_table()
    result = safe_query(conn, "Alice")
    assert len(result) == 1
    assert result[0][1] == "Alice"


def test_safe_query_sql_injection():
    conn = create_table()
    malicious_input = "Alice'; DROP TABLE users; --"

    # Safe query должен выполниться без ошибок и не удалить таблицу
    result = safe_query(conn, malicious_input)
    assert len(result) == 0  # Такого пользователя нет