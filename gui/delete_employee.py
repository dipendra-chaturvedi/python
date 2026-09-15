import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title("Employee Management")
window.geometry("500x300")

employee_list = tk.Listbox(window)

employees = [
    "Dipendra - 75000",
    "Rahul - 55000",
    "Andrul - 60000"
]

for employee in employees:
    employee_list.insert(tk.END, employee)

employee_list.pack()

def delete_employee():
    selected = employee_list.curselection()

    if selected:
        employee_list.delete(selected[0])
        messagebox.showinfo("Success", "Employee deleted")

tk.Button(
    window,
    text="Delete Employee",
    command=delete_employee
).pack()

window.mainloop()