import tkinter as tk
from tkinter import ttk
import sqlite3

window = tk.Tk()
window.title("Employee Management")
window.geometry("600x300")

table = ttk.Treeview(
    window,
    columns=("ID", "Name", "Salary"),
    show="headings"
)

table.heading("ID", text="ID")
table.heading("Name", text="Name")
table.heading("Salary", text="Salary")

table.pack(fill="both", expand=True)

connection = sqlite3.connect(
    r"C:\Development\python\gui\employees.db"
)

cursor = connection.cursor()

cursor.execute("SELECT id, name, salary FROM employees")

for employee in cursor.fetchall():
    table.insert("", tk.END, values=employee)

connection.close()

window.mainloop()