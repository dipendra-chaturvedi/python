import sqlite3
import os

current_folder = os.path.dirname(__file__)

db_path = os.path.join(current_folder, "employee.db")

conn = sqlite3.connect(db_path)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY,
    name TEXT,
    department TEXT,
    salary REAL
)
""")

cursor.execute("""
INSERT INTO employees (name, department, salary)
VALUES (?, ?, ?)
""", ("Dipendra", "Developer", 60000))

conn.commit()

print("Employee Saved Successfully")

conn.close()

# Read Data
# import sqlite3
# import os

# current_folder = os.path.dirname(__file__)

# db_path = os.path.join(current_folder, "employee.db")

# conn = sqlite3.connect(db_path)

# cursor = conn.cursor()

# cursor.execute("SELECT * FROM employees")

# employees = cursor.fetchall()

# for employee in employees:
#     print(employee)

# conn.close()

# sqlite3.connect()
# cursor()
# execute()
# executemany()
# fetchone()
# fetchall()
# commit()
# close()