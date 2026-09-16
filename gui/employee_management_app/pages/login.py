import tkinter as tk
from tkinter import messagebox
import sqlite3
import os


BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

DB_PATH = os.path.join(
    BASE_DIR,
    "database",
    "employee.db"
)

APP_PATH = os.path.join(
    BASE_DIR,
    "pages"
)


def open_dashboard():

    import subprocess

    subprocess.Popen([
        "python",
        f"{APP_PATH}\\dashboard.py"
    ])

    window.destroy()


def open_register():

    import subprocess

    subprocess.Popen([
        "python",
        f"{APP_PATH}\\register.py"
    ])

    window.destroy()


def login():

    username = username_entry.get()
    password = password_entry.get()

    if not username or not password:
        messagebox.showerror(
            "Login",
            "Username and password are required"
        )
        return

    connection = sqlite3.connect(DB_PATH)

    cursor = connection.cursor()

    cursor.execute(
        "SELECT * FROM users WHERE username = ? AND password = ?",
        (username, password)
    )

    user = cursor.fetchone()

    connection.close()

    if user:
        open_dashboard()

    else:
        messagebox.showerror(
            "Login",
            "Invalid username or password"
        )


# ---------------- WINDOW ----------------

window = tk.Tk()

window.title("Employee Management - Login")
window.geometry("900x600")
window.configure(bg="#f3f4f6")


# ---------------- LEFT PANEL ----------------

left_panel = tk.Frame(
    window,
    bg="#1f2937",
    width=350
)

left_panel.pack(
    side="left",
    fill="y"
)

left_panel.pack_propagate(False)


tk.Label(
    left_panel,
    text="Employee",
    bg="#1f2937",
    fg="white",
    font=("Arial", 28, "bold")
).pack(
    pady=(150, 5)
)


tk.Label(
    left_panel,
    text="Management System",
    bg="#1f2937",
    fg="#d1d5db",
    font=("Arial", 15)
).pack()


tk.Label(
    left_panel,
    text="Manage your employees\nquickly and easily",
    bg="#1f2937",
    fg="#9ca3af",
    font=("Arial", 11),
    justify="center"
).pack(
    pady=30
)


# ---------------- RIGHT PANEL ----------------

right_panel = tk.Frame(
    window,
    bg="#f3f4f6"
)

right_panel.pack(
    side="left",
    fill="both",
    expand=True
)


# ---------------- LOGIN CARD ----------------

login_card = tk.Frame(
    right_panel,
    bg="white",
    padx=45,
    pady=40
)

login_card.pack(
    padx=60,
    pady=100
)


tk.Label(
    login_card,
    text="Welcome Back",
    bg="white",
    fg="#111827",
    font=("Arial", 22, "bold")
).pack(
    anchor="w",
    pady=(0, 8)
)


tk.Label(
    login_card,
    text="Login to your account",
    bg="white",
    fg="#6b7280",
    font=("Arial", 10)
).pack(
    anchor="w",
    pady=(0, 25)
)


# ---------------- USERNAME ----------------

tk.Label(
    login_card,
    text="Username",
    bg="white",
    fg="#374151",
    font=("Arial", 10, "bold")
).pack(
    anchor="w",
    pady=(5, 5)
)


username_entry = tk.Entry(
    login_card,
    width=35,
    font=("Arial", 11),
    bd=1,
    relief="solid"
)

username_entry.pack(
    ipady=8,
    pady=(0, 18)
)


# ---------------- PASSWORD ----------------

tk.Label(
    login_card,
    text="Password",
    bg="white",
    fg="#374151",
    font=("Arial", 10, "bold")
).pack(
    anchor="w",
    pady=(5, 5)
)


password_entry = tk.Entry(
    login_card,
    width=35,
    font=("Arial", 11),
    show="*",
    bd=1,
    relief="solid"
)

password_entry.pack(
    ipady=8,
    pady=(0, 25)
)


# ---------------- LOGIN BUTTON ----------------

tk.Button(
    login_card,
    text="Login",
    command=login,
    bg="#2563eb",
    fg="white",
    activebackground="#1d4ed8",
    activeforeground="white",
    bd=0,
    font=("Arial", 11, "bold"),
    width=30,
    pady=10,
    cursor="hand2"
).pack()


# ---------------- REGISTER LINK ----------------

tk.Button(
    login_card,
    text="Don't have an account? Register",
    command=open_register,
    bg="white",
    fg="#2563eb",
    activebackground="white",
    activeforeground="#1d4ed8",
    bd=0,
    font=("Arial", 10),
    cursor="hand2"
).pack(
    pady=(18, 0)
)


window.mainloop()