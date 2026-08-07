from models.employee import Employee

# Insert Code 
from database.db import save_employee

emp = Employee(102, "Andrul", 60000)
save_employee(emp)

# Get Code
# from database.db import get_employees

# employees = get_employees()
# for employee in employees:
#     print(employee)

# Update Code
# from database.db import update_employee_salary

# update_employee_salary(1, 75000)

# Delete Code
# from database.db import delete_employee

# delete_employee(2)