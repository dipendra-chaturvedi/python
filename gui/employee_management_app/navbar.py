import tkinter as tk

window = tk.Tk()
window.title("Employee Management System")
window.geometry("800x500")

navbar = tk.Frame(window)
navbar.pack(fill="x")

tk.Button(navbar, text="Dashboard").pack(side="left")
tk.Button(navbar, text="Employees").pack(side="left")
tk.Button(navbar, text="Add Employee").pack(side="left")
tk.Button(navbar, text="Profile").pack(side="left")
tk.Button(navbar, text="Logout").pack(side="right")

window.mainloop()