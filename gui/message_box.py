import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title("Employee Management")
window.geometry("500x300")


def save_employee():
    messagebox.showinfo(
        "Success",
        "Employee saved successfully"
    )

tk.Button(
    window,
    text="Save Employee",
    command=save_employee
).pack()

window.mainloop()