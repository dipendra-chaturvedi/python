import tkinter as tk
from tkinter import messagebox
import subprocess


APP_PATH = r"C:\Development\python\gui\employee_management_app\pages"


def open_page(file_name):
    subprocess.Popen([
        "python",
        f"{APP_PATH}\\{file_name}"
    ])


def open_employees():
    open_page("view_employee.py")


def open_add_employee():
    open_page("add_employee.py")


def open_profile():
    open_page("profile.py")


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
window.title("Employee Management System")
window.geometry("1000x600")
window.minsize(900, 550)


# ---------------- COLORS ----------------

SIDEBAR = "#1f2937"
SIDEBAR_HOVER = "#374151"
BACKGROUND = "#f3f4f6"
WHITE = "#ffffff"
TEXT = "#111827"
SECONDARY = "#6b7280"


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


# Logo / Title

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


# Sidebar buttons

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

    return button


sidebar_button("▣   Dashboard", lambda: None)
sidebar_button("👥  Employees", open_employees)
sidebar_button("+   Add Employee", open_add_employee)
sidebar_button("◉   Profile", open_profile)

tk.Frame(
    sidebar,
    bg=SIDEBAR,
    height=100
).pack(fill="x")

sidebar_button("↪   Logout", logout)


# ---------------- MAIN AREA ----------------

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

topbar.pack(
    fill="x"
)

topbar.pack_propagate(False)


tk.Label(
    topbar,
    text="Dashboard",
    bg=WHITE,
    fg=TEXT,
    font=("Arial", 22, "bold")
).pack(
    side="left",
    padx=30
)


tk.Label(
    topbar,
    text="Welcome, Admin",
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


tk.Label(
    content,
    text="Welcome back!",
    bg=BACKGROUND,
    fg=TEXT,
    font=("Arial", 24, "bold")
).pack(anchor="w")


tk.Label(
    content,
    text="Manage your employees from one place.",
    bg=BACKGROUND,
    fg=SECONDARY,
    font=("Arial", 11)
).pack(
    anchor="w",
    pady=(5, 25)
)


# ---------------- STAT CARDS ----------------

cards = tk.Frame(
    content,
    bg=BACKGROUND
)

cards.pack(
    fill="x"
)


def create_card(parent, title, value, subtitle):
    card = tk.Frame(
        parent,
        bg=WHITE,
        height=130
    )

    card.pack(
        side="left",
        fill="both",
        expand=True,
        padx=7
    )

    card.pack_propagate(False)

    tk.Label(
        card,
        text=title,
        bg=WHITE,
        fg=SECONDARY,
        font=("Arial", 10)
    ).pack(
        anchor="w",
        padx=20,
        pady=(20, 5)
    )

    tk.Label(
        card,
        text=value,
        bg=WHITE,
        fg=TEXT,
        font=("Arial", 25, "bold")
    ).pack(
        anchor="w",
        padx=20
    )

    tk.Label(
        card,
        text=subtitle,
        bg=WHITE,
        fg=SECONDARY,
        font=("Arial", 9)
    ).pack(
        anchor="w",
        padx=20
    )


create_card(
    cards,
    "TOTAL EMPLOYEES",
    "3",
    "Registered employees"
)

create_card(
    cards,
    "ACTIVE",
    "2",
    "Currently active"
)

create_card(
    cards,
    "INACTIVE",
    "1",
    "Currently inactive"
)


# ---------------- QUICK ACTIONS ----------------

tk.Label(
    content,
    text="Quick Actions",
    bg=BACKGROUND,
    fg=TEXT,
    font=("Arial", 16, "bold")
).pack(
    anchor="w",
    pady=(35, 15)
)


actions = tk.Frame(
    content,
    bg=BACKGROUND
)

actions.pack(
    fill="x"
)


tk.Button(
    actions,
    text="+  Add Employee",
    command=open_add_employee,
    bg="#2563eb",
    fg=WHITE,
    activebackground="#1d4ed8",
    activeforeground=WHITE,
    font=("Arial", 11, "bold"),
    relief="flat",
    padx=25,
    pady=12
).pack(
    side="left",
    padx=(0, 10)
)


tk.Button(
    actions,
    text="👥  View Employees",
    command=open_employees,
    bg=WHITE,
    fg=TEXT,
    activebackground="#e5e7eb",
    relief="flat",
    font=("Arial", 11),
    padx=25,
    pady=12
).pack(
    side="left"
)


window.mainloop()