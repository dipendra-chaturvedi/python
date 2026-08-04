import os

project_folder = os.path.dirname(__file__)

employee_folder = os.path.join(project_folder, "employees")

if not os.path.exists(employee_folder):
    os.mkdir(employee_folder)

employee_id = input("Employee ID: ")
employee_name = input("Employee Name: ")
employee_salary = input("Employee Salary: ")

employee_file = os.path.join(employee_folder, f"{employee_id}.txt")

with open(employee_file, "w", encoding="utf-8") as file:
    file.write(f"ID : {employee_id}\n")
    file.write(f"Name : {employee_name}\n")
    file.write(f"Salary : {employee_salary}\n")

print(f"Employee {employee_id} saved successfully.")