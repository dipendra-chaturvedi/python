import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
import subprocess


DB_PATH = r"C:\Development\python\gui\employee_management_app\database\employee.db"
APP_PATH = r"C:\Development\python\gui\employee_management_app\pages"


SIDEBAR = "#1f2937"
SIDEBAR_HOVER = "#374151"
BACKGROUND = "#f3f4f6"
WHITE = "#ffffff"
TEXT = "#111827"
SECONDARY = "#6b7280"


def open_page(file_name):
    subprocess.Popen([
        "python",
        f"{APP_PATH}\\{file_name}"
    ])


def get_selected_employee():
    selected = table.selection()

    if not selected:
        messagebox.showerror(
            "Error",
            "Please select an employee first"
        )
        return None

    return table.item(selected[0], "values")


def view_employee():
    employee = get_selected_employee()

    if employee:
        messagebox.showinfo(
            "Employee Details",
            f"Employee ID: {employee[0]}\n\n"
            f"Name: {employee[1]}\n"
            f"Salary: ₹{employee[2]}\n"
            f"Department: {employee[3]}\n"
            f"Status: {employee[4]}"
        )


def edit_employee():
    employee = get_selected_employee()

    if employee:
        open_page("edit_employee.py")


def delete_employee():
    employee = get_selected_employee()

    if not employee:
        return

    confirm = messagebox.askyesno(
        "Confirm Delete",
        f"Are you sure you want to delete {employee[1]}?"
    )

    if not confirm:
        return

    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()

    cursor.execute(
        "DELETE FROM employees WHERE id = ?",
        (employee[0],)
    )

    connection.commit()
    connection.close()

    table.delete(table.selection())

    messagebox.showinfo(
        "Success",
        "Employee deleted successfully"
    )


def refresh_table():
    for item in table.get_children():
        table.delete(item)

    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()

    cursor.execute(
        "SELECT id, name, salary, department, status FROM employees"
    )

    for employee in cursor.fetchall():
        table.insert("", tk.END, values=employee)

    connection.close()


def logout():
    confirm = messagebox.askyesno(
        "Logout",
        "Are you sure you want to logout?"
    )

    if confirm:
        window.destroy()
        open_page("login.py")


# ---------------- WINDOW ----------------

window = tk.Tk()
window.title("Employee Management - Employees")
window.geometry("1100x650")
window.minsize(950, 550)

window.configure(bg=BACKGROUND)


# ---------------- SIDEBAR ----------------

sidebar = tk.Frame(
    window,
    bg=SIDEBAR,
    width=220
)

sidebar.pack(
    side="left",
    fill="y"
)

sidebar.pack_propagate(False)


tk.Label(
    sidebar,
    text="EMPLOYEE",
    bg=SIDEBAR,
    fg=WHITE,
    font=("Arial", 20, "bold")
).pack(pady=(35, 0))

tk.Label(
    sidebar,
    text="MANAGEMENT",
    bg=SIDEBAR,
    fg="#9ca3af",
    font=("Arial", 10)
).pack(pady=(0, 35))


def sidebar_button(text, command):
    button = tk.Button(
        sidebar,
        text=text,
        command=command,
        bg=SIDEBAR,
        fg=WHITE,
        activebackground=SIDEBAR_HOVER,
        activeforeground=WHITE,
        relief="flat",
        borderwidth=0,
        anchor="w",
        padx=25,
        font=("Arial", 11)
    )

    button.pack(
        fill="x",
        ipady=10,
        pady=2
    )


sidebar_button(
    "▣   Dashboard",
    lambda: open_page("dashboard.py")
)

sidebar_button(
    "👥  Employees",
    lambda: None
)

sidebar_button(
    "+   Add Employee",
    lambda: open_page("add_employee.py")
)

sidebar_button(
    "◉   Profile",
    lambda: open_page("profile.py")
)

tk.Frame(
    sidebar,
    bg=SIDEBAR,
    height=100
).pack(fill="x")

sidebar_button(
    "↪   Logout",
    logout
)


# ---------------- MAIN ----------------

main = tk.Frame(
    window,
    bg=BACKGROUND
)

main.pack(
    side="left",
    fill="both",
    expand=True
)


# ---------------- TOP BAR ----------------

topbar = tk.Frame(
    main,
    bg=WHITE,
    height=70
)

topbar.pack(fill="x")
topbar.pack_propagate(False)


tk.Label(
    topbar,
    text="Employees",
    bg=WHITE,
    fg=TEXT,
    font=("Arial", 22, "bold")
).pack(
    side="left",
    padx=30
)


tk.Label(
    topbar,
    text="Employee Management",
    bg=WHITE,
    fg=SECONDARY,
    font=("Arial", 10)
).pack(
    side="right",
    padx=30
)


# ---------------- CONTENT ----------------

content = tk.Frame(
    main,
    bg=BACKGROUND
)

content.pack(
    fill="both",
    expand=True,
    padx=30,
    pady=25
)


# Header

header = tk.Frame(
    content,
    bg=BACKGROUND
)

header.pack(fill="x")


tk.Label(
    header,
    text="Employee List",
    bg=BACKGROUND,
    fg=TEXT,
    font=("Arial", 18, "bold")
).pack(side="left")


tk.Button(
    header,
    text="+ Add Employee",
    command=lambda: open_page("add_employee.py"),
    bg="#2563eb",
    fg=WHITE,
    activebackground="#1d4ed8",
    activeforeground=WHITE,
    relief="flat",
    font=("Arial", 10, "bold"),
    padx=18,
    pady=8
).pack(side="right")


# ---------------- TABLE CARD ----------------

table_card = tk.Frame(
    content,
    bg=WHITE
)

table_card.pack(
    fill="both",
    expand=True,
    pady=20
)


table = ttk.Treeview(
    table_card,
    columns=(
        "ID",
        "Name",
        "Salary",
        "Department",
        "Status"
    ),
    show="headings"
)


table.heading("ID", text="ID")
table.heading("Name", text="NAME")
table.heading("Salary", text="SALARY")
table.heading("Department", text="DEPARTMENT")
table.heading("Status", text="STATUS")


table.column("ID", width=60, anchor="center")
table.column("Name", width=180)
table.column("Salary", width=150)
table.column("Department", width=150)
table.column("Status", width=120, anchor="center")


table.pack(
    fill="both",
    expand=True,
    padx=15,
    pady=15
)


# ---------------- BUTTONS ----------------

button_frame = tk.Frame(
    content,
    bg=BACKGROUND
)

button_frame.pack(
    fill="x"
)


tk.Button(
    button_frame,
    text="View",
    command=view_employee,
    bg=WHITE,
    fg=TEXT,
    relief="flat",
    font=("Arial", 10),
    padx=20,
    pady=8
).pack(side="left", padx=(0, 8))


tk.Button(
    button_frame,
    text="Edit",
    command=edit_employee,
    bg=WHITE,
    fg=TEXT,
    relief="flat",
    font=("Arial", 10),
    padx=20,
    pady=8
).pack(side="left", padx=8)


tk.Button(
    button_frame,
    text="Delete",
    command=delete_employee,
    bg="#dc2626",
    fg=WHITE,
    activebackground="#b91c1c",
    activeforeground=WHITE,
    relief="flat",
    font=("Arial", 10),
    padx=20,
    pady=8
).pack(side="left", padx=8)


tk.Button(
    button_frame,
    text="Refresh",
    command=refresh_table,
    bg=WHITE,
    fg=TEXT,
    relief="flat",
    font=("Arial", 10),
    padx=20,
    pady=8
).pack(side="right")


# Load employees

refresh_table()


window.mainloop()