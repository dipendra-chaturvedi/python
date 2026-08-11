from flask import Flask, request
# from employees import get_all_employees, get_employee_by_id, add_employee
from employees import (
    get_all_employees,
    get_employee_by_id,
    add_employee,
    update_employee,
    delete_employee
)

app = Flask(__name__)

# Home route
@app.route("/")
def home():
    return {
        "message": "REST API is running"
    }, 200

# Employees routes
@app.route("/employees", methods=["GET"])
def employees():
    return get_all_employees(), 200




# Get employee by ID route
# @app.route("/employees/<int:employee_id>", methods=["GET"])
# def get_employee(employee_id):

#     employee = get_employee_by_id(employee_id)

#     if employee is None:
#         return {
#             "message": "Employee not found"
#         }, 404

#     return employee, 200

# Get employee by ID route with success response
@app.route("/employees/<int:employee_id>", methods=["GET"])
def get_employee(employee_id):

    employee = get_employee_by_id(employee_id)

    if employee is None:
        return {
            "success": False,
            "message": "Employee not found"
        }, 404

    return {
        "success": True,
        "data": employee
    }, 200


# Add employee route
# @app.route("/employees", methods=["POST"])
# def create_employee():

#     data = request.get_json()

#     new_employee = {
#         "id": data["id"],
#         "name": data["name"],
#         "salary": data["salary"]
#     }

#     employee = add_employee(new_employee)

#     return employee, 201

# Add employee route with validation & error handling
# @app.route("/employees", methods=["POST"])
# def create_employee():

#     data = request.get_json()

#     if not data:
#         return {
#             "message": "JSON data is required"
#         }, 400

#     if "id" not in data or "name" not in data or "salary" not in data:
#         return {
#             "message": "id, name and salary are required"
#         }, 400

#     if not isinstance(data["id"], int):
#         return {
#             "message": "id must be an integer"
#         }, 400

#     if not isinstance(data["name"], str) or not data["name"].strip():
#         return {
#             "message": "name must be a non-empty string"
#         }, 400

#     if not isinstance(data["salary"], (int, float)) or data["salary"] <= 0:
#         return {
#             "message": "salary must be greater than 0"
#         }, 400

#     existing_employee = get_employee_by_id(data["id"])

#     if existing_employee is not None:
#         return {
#             "message": "Employee ID already exists"
#         }, 400

#     new_employee = {
#         "id": data["id"],
#         "name": data["name"],
#         "salary": data["salary"]
#     }

#     employee = add_employee(new_employee)

#     return employee, 201

# Add employee route validation with try-except block 
@app.route("/employees", methods=["POST"])
def create_employee():

    try:
        data = request.get_json()

        if not data:
            return {
                "message": "JSON data is required"
            }, 400

        if "id" not in data or "name" not in data or "salary" not in data:
            return {
                "message": "id, name and salary are required"
            }, 400

        if not isinstance(data["id"], int):
            return {
                "message": "id must be an integer"
            }, 400

        if not isinstance(data["name"], str) or not data["name"].strip():
            return {
                "message": "name must be a non-empty string"
            }, 400

        if not isinstance(data["salary"], (int, float)) or data["salary"] <= 0:
            return {
                "message": "salary must be greater than 0"
            }, 400

        existing_employee = get_employee_by_id(data["id"])

        if existing_employee is not None:
            return {
                "message": "Employee ID already exists"
            }, 400

        new_employee = {
            "id": data["id"],
            "name": data["name"],
            "salary": data["salary"]
        }

        employee = add_employee(new_employee)

        return employee, 201

    except Exception:
        return {
            "message": "Internal server error"
        }, 500

# Update employee route
@app.route("/employees/<int:employee_id>", methods=["PUT"])
def edit_employee(employee_id):

    data = request.get_json()

    employee = update_employee(employee_id, data)

    if employee is None:
        return {
            "message": "Employee not found"
        }, 404

    return employee, 200

# Delete employee route
@app.route("/employees/<int:employee_id>", methods=["DELETE"])
def remove_employee(employee_id):

    employee = delete_employee(employee_id)

    if employee is None:
        return {
            "message": "Employee not found"
        }, 404

    return {
        "message": "Employee deleted successfully"
    }, 200

if __name__ == "__main__":
    app.run(debug=True)