import os
import csv

current_folder = os.path.dirname(__file__)

file_path = os.path.join(current_folder, "employees.csv")

employee = [101, "Dipendra", "Developer", 60000]

with open(file_path, "a", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(employee)

print("Employee Saved Successfully")