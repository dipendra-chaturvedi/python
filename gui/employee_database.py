import tkinter as tk
from tkinter import messagebox
import sqlite3

window = tk.Tk()
window.title("Employee Management")
window.geometry("500x300")

connection = sqlite3.connect(
    r"C:\Development\python\gui\employees.db"
)

cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    salary REAL
)
""")

connection.commit()


tk.Label(window, text="Employee Name").pack()

name_entry = tk.Entry(window)
name_entry.pack()

tk.Label(window, text="Salary").pack()

salary_entry = tk.Entry(window)
salary_entry.pack()


def save_employee():
    name = name_entry.get()
    salary = salary_entry.get()

    if not name or not salary.isdigit():
        messagebox.showerror("Error", "Enter valid employee details")
        return

    cursor.execute(
        "INSERT INTO employees (name, salary) VALUES (?, ?)",
        (name, salary)
    )

    connection.commit()

    messagebox.showinfo("Success", "Employee saved")


tk.Button(
    window,
    text="Save Employee",
    command=save_employee
).pack()

window.mainloop()