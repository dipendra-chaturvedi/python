import sqlite3

connection = sqlite3.connect(
    r"C:\Development\python\gui\employee_management_app\database\employee.db"
)

cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE,
    password TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    salary REAL NOT NULL,
    department TEXT,
    status TEXT
)
""")

connection.commit()
connection.close()

print("Database ready")