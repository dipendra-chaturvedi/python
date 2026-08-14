import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="employee_db",
    use_pure=True
)

cursor = connection.cursor()

name = input("Enter employee name: ")

query = """
SELECT * FROM employees
WHERE name = %s
"""

cursor.execute(query, (name,))

employees = cursor.fetchall()

for employee in employees:
    print(employee)

cursor.close()
connection.close()