import tkinter as tk

window = tk.Tk()
window.title("Employee Management")
window.geometry("500x300")

tk.Label(window, text="Employee Name:").pack()

name_entry = tk.Entry(window)
name_entry.pack()


def show_employee():
    name = name_entry.get()
    print("Employee:", name)


tk.Button(
    window,
    text="Save Employee",
    command=show_employee
).pack()

window.mainloop()