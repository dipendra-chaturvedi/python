import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3


DB_PATH = r"C:\Development\python\gui\employee_management_app\database\employee.db"
APP_PATH = r"C:\Development\python\gui\employee_management_app\pages"


def open_page(file_name):
    import subprocess

    subprocess.Popen([
        "python",
        f"{APP_PATH}\\{file_name}"
    ])

    window.destroy()


def save_employee():

    name = name_entry.get()
    salary = salary_entry.get()
    department_value = department.get()
    status_value = status.get()

    if not name or not salary or not department_value or not status_value:
        messagebox.showerror(
            "Error",
            "All fields are required"
        )
        return

    try:
        salary_value = float(salary)
    except ValueError:
        messagebox.showerror(
            "Error",
            "Salary must be a number"
        )
        return

    connection = sqlite3.connect(DB_PATH)

    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO employees
        (name, salary, department, status)
        VALUES (?, ?, ?, ?)
        """,
        (
            name,
            salary_value,
            department_value,
            status_value
        )
    )

    connection.commit()
    connection.close()

    messagebox.showinfo(
        "Success",
        "Employee saved successfully"
    )

    name_entry.delete(0, tk.END)
    salary_entry.delete(0, tk.END)
    department.set("")
    status.set("")


def logout():

    result = messagebox.askyesno(
        "Logout",
        "Are you sure you want to logout?"
    )

    if result:
        open_page("login.py")


# ---------------- WINDOW ----------------

window = tk.Tk()

window.title("Add Employee")
window.geometry("1100x650")
window.configure(bg="#f3f4f6")


# ---------------- SIDEBAR ----------------

sidebar = tk.Frame(
    window,
    bg="#1f2937",
    width=220
)

sidebar.pack(
    side="left",
    fill="y"
)

sidebar.pack_propagate(False)


tk.Label(
    sidebar,
    text="Employee Management",
    bg="#1f2937",
    fg="white",
    font=("Arial", 16, "bold")
).pack(pady=30)


def sidebar_button(text, command):

    tk.Button(
        sidebar,
        text=text,
        command=command,
        bg="#1f2937",
        fg="white",
        activebackground="#374151",
        activeforeground="white",
        bd=0,
        anchor="w",
        padx=25,
        font=("Arial", 11),
        height=2
    ).pack(
        fill="x",
        pady=2
    )


sidebar_button(
    "Dashboard",
    lambda: open_page("dashboard.py")
)

sidebar_button(
    "Employees",
    lambda: open_page("view_employee.py")
)

sidebar_button(
    "Add Employee",
    lambda: open_page("add_employee.py")
)

sidebar_button(
    "Profile",
    lambda: open_page("profile.py")
)

sidebar_button(
    "Logout",
    logout
)


# ---------------- MAIN AREA ----------------

main_area = tk.Frame(
    window,
    bg="#f3f4f6"
)

main_area.pack(
    side="left",
    fill="both",
    expand=True
)


# ---------------- TOP BAR ----------------

topbar = tk.Frame(
    main_area,
    bg="white",
    height=70
)

topbar.pack(
    fill="x"
)

topbar.pack_propagate(False)


tk.Label(
    topbar,
    text="Add Employee",
    bg="white",
    fg="#111827",
    font=("Arial", 20, "bold")
).pack(
    side="left",
    padx=30,
    pady=20
)


# ---------------- FORM CARD ----------------

form_card = tk.Frame(
    main_area,
    bg="white",
    padx=40,
    pady=30
)

form_card.pack(
    padx=60,
    pady=50,
    fill="x"
)


tk.Label(
    form_card,
    text="Employee Information",
    bg="white",
    fg="#111827",
    font=("Arial", 16, "bold")
).grid(
    row=0,
    column=0,
    columnspan=2,
    sticky="w",
    pady=(0, 25)
)


# Employee Name

tk.Label(
    form_card,
    text="Employee Name",
    bg="white",
    fg="#374151",
    font=("Arial", 11)
).grid(
    row=1,
    column=0,
    sticky="w",
    pady=10
)

name_entry = tk.Entry(
    form_card,
    font=("Arial", 11),
    width=35
)

name_entry.grid(
    row=1,
    column=1,
    padx=30,
    pady=10
)


# Salary

tk.Label(
    form_card,
    text="Salary",
    bg="white",
    fg="#374151",
    font=("Arial", 11)
).grid(
    row=2,
    column=0,
    sticky="w",
    pady=10
)

salary_entry = tk.Entry(
    form_card,
    font=("Arial", 11),
    width=35
)

salary_entry.grid(
    row=2,
    column=1,
    padx=30,
    pady=10
)


# Department

tk.Label(
    form_card,
    text="Department",
    bg="white",
    fg="#374151",
    font=("Arial", 11)
).grid(
    row=3,
    column=0,
    sticky="w",
    pady=10
)

department = ttk.Combobox(
    form_card,
    values=[
        "IT",
        "HR",
        "Finance",
        "Testing"
    ],
    width=33,
    state="readonly"
)

department.grid(
    row=3,
    column=1,
    padx=30,
    pady=10
)


# Status

tk.Label(
    form_card,
    text="Status",
    bg="white",
    fg="#374151",
    font=("Arial", 11)
).grid(
    row=4,
    column=0,
    sticky="w",
    pady=10
)

status = ttk.Combobox(
    form_card,
    values=[
        "Active",
        "Inactive"
    ],
    width=33,
    state="readonly"
)

status.grid(
    row=4,
    column=1,
    padx=30,
    pady=10
)


# ---------------- SAVE BUTTON ----------------

tk.Button(
    form_card,
    text="Save Employee",
    command=save_employee,
    bg="#2563eb",
    fg="white",
    activebackground="#1d4ed8",
    activeforeground="white",
    bd=0,
    font=("Arial", 11, "bold"),
    padx=25,
    pady=10
).grid(
    row=5,
    column=0,
    columnspan=2,
    pady=30
)


window.mainloop()