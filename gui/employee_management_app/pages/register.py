import tkinter as tk
from tkinter import messagebox
import sqlite3


DB_PATH = r"C:\Development\python\gui\employee_management_app\database\employee.db"
APP_PATH = r"C:\Development\python\gui\employee_management_app\pages"


def open_login():
    import subprocess

    subprocess.Popen([
        "python",
        f"{APP_PATH}\\login.py"
    ])

    window.destroy()


def register():

    username = username_entry.get()
    password = password_entry.get()
    confirm_password = confirm_entry.get()

    if not username or not password or not confirm_password:
        messagebox.showerror(
            "Error",
            "All fields are required"
        )
        return

    if password != confirm_password:
        messagebox.showerror(
            "Error",
            "Passwords do not match"
        )
        return

    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()

    try:

        cursor.execute(
            "INSERT INTO users (username, password) VALUES (?, ?)",
            (username, password)
        )

        connection.commit()

        messagebox.showinfo(
            "Success",
            "Registration successful"
        )

        open_login()

    except sqlite3.IntegrityError:

        messagebox.showerror(
            "Error",
            "Username already exists"
        )

    finally:
        connection.close()


# ---------------- WINDOW ----------------

window = tk.Tk()

window.title("Employee Management - Register")
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
).pack(pady=(150, 5))


tk.Label(
    left_panel,
    text="Management System",
    bg="#1f2937",
    fg="#d1d5db",
    font=("Arial", 15)
).pack()


tk.Label(
    left_panel,
    text="Create your account\nto continue",
    bg="#1f2937",
    fg="#9ca3af",
    font=("Arial", 11),
    justify="center"
).pack(pady=30)


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


# ---------------- REGISTER CARD ----------------

register_card = tk.Frame(
    right_panel,
    bg="white",
    padx=45,
    pady=35
)

register_card.pack(
    padx=60,
    pady=70
)


tk.Label(
    register_card,
    text="Create Account",
    bg="white",
    fg="#111827",
    font=("Arial", 22, "bold")
).pack(
    anchor="w",
    pady=(0, 8)
)


tk.Label(
    register_card,
    text="Register a new user account",
    bg="white",
    fg="#6b7280",
    font=("Arial", 10)
).pack(
    anchor="w",
    pady=(0, 25)
)


# ---------------- USERNAME ----------------

tk.Label(
    register_card,
    text="Username",
    bg="white",
    fg="#374151",
    font=("Arial", 10, "bold")
).pack(
    anchor="w",
    pady=(5, 5)
)


username_entry = tk.Entry(
    register_card,
    width=35,
    font=("Arial", 11),
    bd=1,
    relief="solid"
)

username_entry.pack(
    ipady=8,
    pady=(0, 15)
)


# ---------------- PASSWORD ----------------

tk.Label(
    register_card,
    text="Password",
    bg="white",
    fg="#374151",
    font=("Arial", 10, "bold")
).pack(
    anchor="w",
    pady=(5, 5)
)


password_entry = tk.Entry(
    register_card,
    width=35,
    font=("Arial", 11),
    show="*",
    bd=1,
    relief="solid"
)

password_entry.pack(
    ipady=8,
    pady=(0, 15)
)


# ---------------- CONFIRM PASSWORD ----------------

tk.Label(
    register_card,
    text="Confirm Password",
    bg="white",
    fg="#374151",
    font=("Arial", 10, "bold")
).pack(
    anchor="w",
    pady=(5, 5)
)


confirm_entry = tk.Entry(
    register_card,
    width=35,
    font=("Arial", 11),
    show="*",
    bd=1,
    relief="solid"
)

confirm_entry.pack(
    ipady=8,
    pady=(0, 25)
)


# ---------------- REGISTER BUTTON ----------------

tk.Button(
    register_card,
    text="Create Account",
    command=register,
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


# ---------------- LOGIN LINK ----------------

tk.Button(
    register_card,
    text="Already have an account? Login",
    command=open_login,
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