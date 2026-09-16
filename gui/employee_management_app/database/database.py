import sqlite3
import os


# Project root:
# employee_management_app/
BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)


# Database location
DB_PATH = os.path.join(
    BASE_DIR,
    "database",
    "employee.db"
)


connection = sqlite3.connect(DB_PATH)

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