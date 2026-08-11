employees = [
    {
        "id": 1,
        "name": "Dipendra",
        "salary": 75000
    },
    {
        "id": 2,
        "name": "Rahul",
        "salary": 55000
    }
]


# Get all employees
def get_all_employees():
    return employees

# Get employee by ID
def get_employee_by_id(employee_id):

    for employee in employees:
        if employee["id"] == employee_id:
            return employee

    return None

# Add a new employee
def add_employee(employee):
    employees.append(employee)
    return employee

# Update an existing employee
def update_employee(employee_id, new_data):

    for employee in employees:

        if employee["id"] == employee_id:
            employee["name"] = new_data["name"]
            employee["salary"] = new_data["salary"]

            return employee

    return None

# Delete an employee
def delete_employee(employee_id):

    for employee in employees:

        if employee["id"] == employee_id:
            employees.remove(employee)
            return employee

    return None