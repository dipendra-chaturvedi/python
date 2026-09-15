import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title("Employee Management")
window.geometry("500x300")

tk.Label(window, text="Employee Name").pack()

name_entry = tk.Entry(window)
name_entry.pack()

tk.Label(window, text="Salary").pack()

salary_entry = tk.Entry(window)
salary_entry.pack()

def update_employee():
    name = name_entry.get()
    salary = salary_entry.get()

    if name and salary:
        messagebox.showinfo(
            "Success",
            f"{name}'s salary updated to {salary}"
        )

tk.Button(
    window,
    text="Update Employee",
    command=update_employee
).pack()

window.mainloop()