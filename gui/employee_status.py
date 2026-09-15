import tkinter as tk

window = tk.Tk()
window.title("Employee Management")
window.geometry("500x300")

active = tk.BooleanVar()

tk.Checkbutton(
    window,
    text="Employee is Active",
    variable=active
).pack()


def save_employee():
    print("Active:", active.get())


tk.Button(
    window,
    text="Save",
    command=save_employee
).pack()

window.mainloop()