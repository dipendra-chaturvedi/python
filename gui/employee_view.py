import tkinter as tk
import sqlite3

window = tk.Tk()
window.title("Employee Management")
window.geometry("500x300")

connection = sqlite3.connect(
    r"C:\Development\python\gui\employees.db"
)

cursor = connection.cursor()

cursor.execute("SELECT id, name, salary FROM employees")

employees = cursor.fetchall()

for employee in employees:
    print(employee)

connection.close()

window.mainloop()