import tkinter as tk


window = tk.Tk()
window.title("Employee Profile")
window.geometry("400x300")

tk.Label(
    window,
    text="Employee Profile",
    font=("Arial", 18)
).pack(pady=30)

tk.Label(
    window,
    text="Username: Admin"
).pack(pady=10)

tk.Button(
    window,
    text="Close",
    command=window.destroy
).pack(pady=20)

window.mainloop()