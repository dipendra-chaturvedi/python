import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("Employee Management")
window.geometry("500x300")

tk.Label(window, text="Department:").pack()

department = ttk.Combobox(
    window,
    values=["IT", "HR", "Finance", "Testing"]
)
department.pack()

def show_department():
    print("Department:", department.get())

tk.Button(
    window,
    text="Submit",
    command=show_department
).pack()

window.mainloop()