import os
import json

current_folder = os.path.dirname(__file__)

file_path = os.path.join(current_folder, "employee.json")

employee = {
    "id": 101,
    "name": "Dipendra",
    "department": "Development",
    "salary": 60000
}

with open(file_path, "w", encoding="utf-8") as file:
    json.dump(employee, file, indent=4)

print("Saved at:", file_path)