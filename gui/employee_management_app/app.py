import tkinter as tk


def show_dashboard():
    print("Dashboard clicked")


def show_employees():
    print("Employees clicked")


def add_employee():
    print("Add Employee clicked")


def show_profile():
    print("Profile clicked")


def logout():
    print("Logout clicked")


window = tk.Tk()
window.title("Employee Management System")
window.geometry("800x500")

navbar = tk.Frame(window)
navbar.pack(fill="x")

tk.Button(
    navbar,
    text="Dashboard",
    command=show_dashboard
).pack(side="left")

tk.Button(
    navbar,
    text="Employees",
    command=show_employees
).pack(side="left")

tk.Button(
    navbar,
    text="Add Employee",
    command=add_employee
).pack(side="left")

tk.Button(
    navbar,
    text="Profile",
    command=show_profile
).pack(side="left")

tk.Button(
    navbar,
    text="Logout",
    command=logout
).pack(side="right")


window.mainloop()