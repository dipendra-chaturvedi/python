import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("Employee Management")
window.geometry("600x300")

table = ttk.Treeview(
    window,
    columns=("Name", "Salary", "Department"),
    show="headings"
)

table.heading("Name", text="Name")
table.heading("Salary", text="Salary")
table.heading("Department", text="Department")

employees = [
    ("Dipendra", 75000, "IT"),
    ("Rahul", 55000, "Finance"),
    ("Andrul", 60000, "Testing")
]

for employee in employees:
    table.insert("", tk.END, values=employee)

table.pack(fill="both", expand=True)

window.mainloop()