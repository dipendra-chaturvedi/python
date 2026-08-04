import os

current_folder = os.path.dirname(__file__)


file_path = os.path.join(current_folder, "employees.txt")

employee_name = input("Enter Employee Name: ")
employee_salary = input("Enter Employee Salary: ")

with open(file_path, "a", encoding="utf-8") as file:
    file.write(f"{employee_name} - ₹{employee_salary}\n")

print("Employee Saved Successfully")