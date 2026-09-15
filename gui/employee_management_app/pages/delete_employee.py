import tkinter as tk
from tkinter import messagebox
import sqlite3


def delete_employee():
    employee_id = id_entry.get()

    if not employee_id:
        messagebox.showerror("Error", "Enter Employee ID")
        return

    connection = sqlite3.connect(
        r"C:\Development\python\gui\employee_management_app\database\employee.db"
    )

    cursor = connection.cursor()

    cursor.execute(
        "DELETE FROM employees WHERE id = ?",
        (employee_id,)
    )

    connection.commit()

    if cursor.rowcount == 0:
        messagebox.showerror(
            "Error",
            "Employee not found"
        )
    else:
        messagebox.showinfo(
            "Success",
            "Employee deleted successfully"
        )

    connection.close()


window = tk.Tk()
window.title("Delete Employee")
window.geometry("400x250")

tk.Label(
    window,
    text="Delete Employee",
    font=("Arial", 18)
).pack(pady=30)

tk.Label(window, text="Employee ID").pack()

id_entry = tk.Entry(window)
id_entry.pack()

tk.Button(
    window,
    text="Delete Employee",
    command=delete_employee
).pack(pady=25)

window.mainloop()