import tkinter as tk

window = tk.Tk()
window.title("Employee Management")
window.geometry("500x300")

tk.Label(window, text="Employee Name:").pack()
name_entry = tk.Entry(window)
name_entry.pack()

tk.Label(window, text="Salary:").pack()
salary_entry = tk.Entry(window)
salary_entry.pack()


def save_employee():
    name = name_entry.get()
    salary = salary_entry.get()

    print("Name:", name)
    print("Salary:", salary)


tk.Button(
    window,
    text="Save Employee",
    command=save_employee
).pack()

window.mainloop()