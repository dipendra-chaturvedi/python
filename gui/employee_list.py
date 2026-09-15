import tkinter as tk

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

window.mainloop()