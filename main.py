import sqlite3

# Подключение к базе данных
conn = sqlite3.connect("example.db")
cursor = conn.cursor()

# Получение пользовательского ввода (имитация)
user_input = "Alice'; DROP TABLE users; --"

# Опасное формирование SQL-запроса через f-строку
query = f"SELECT * FROM users WHERE name = '{user_input}'"

# Выполнение запроса (триггер для предупреждения B608)
cursor.execute(query)

# Закрытие соединения
conn.close()