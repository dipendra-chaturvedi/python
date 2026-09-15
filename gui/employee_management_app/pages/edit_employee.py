import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3


def update_employee():
    employee_id = id_entry.get()
    name = name_entry.get()
    salary = salary_entry.get()
    department_value = department.get()
    status_value = status.get()

    if not employee_id or not name or not salary:
        messagebox.showerror("Error", "All fields are required")
        return

    connection = sqlite3.connect(
        r"C:\Development\python\gui\employee_management_app\database\employee.db"
    )

    cursor = connection.cursor()

    cursor.execute(
        """
        UPDATE employees
        SET name = ?, salary = ?, department = ?, status = ?
        WHERE id = ?
        """,
        (
            name,
            salary,
            department_value,
            status_value,
            employee_id
        )
    )

    connection.commit()

    if cursor.rowcount == 0:
        messagebox.showerror("Error", "Employee not found")
    else:
        messagebox.showinfo(
            "Success",
            "Employee updated successfully"
        )

    connection.close()


window = tk.Tk()
window.title("Edit Employee")
window.geometry("400x450")

tk.Label(
    window,
    text="Edit Employee",
    font=("Arial", 18)
).pack(pady=20)

tk.Label(window, text="Employee ID").pack()

id_entry = tk.Entry(window)
id_entry.pack()

tk.Label(window, text="Employee Name").pack()

name_entry = tk.Entry(window)
name_entry.pack()

tk.Label(window, text="Salary").pack()

salary_entry = tk.Entry(window)
salary_entry.pack()

tk.Label(window, text="Department").pack()

department = ttk.Combobox(
    window,
    values=["IT", "HR", "Finance", "Testing"]
)
department.pack()

tk.Label(window, text="Status").pack()

status = ttk.Combobox(
    window,
    values=["Active", "Inactive"]
)
status.pack()

tk.Button(
    window,
    text="Update Employee",
    command=update_employee
).pack(pady=25)

window.mainloop()