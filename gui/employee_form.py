import tkinter as tk

window = tk.Tk()
window.title("Employee Management")
window.geometry("500x300")

tk.Label(window, text="Employee Name:").pack()

name_entry = tk.Entry(window)
name_entry.pack()

window.mainloop()