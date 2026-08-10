from flask import Flask, request 
from database import get_connection

app = Flask(__name__)

@app.route("/")
def home():
    return "Flask is running"

# Static Route
# @app.route("/employees")
# def employees():
#     return "Employee List"

# Dynamic Route
# @app.route("/employees/<int:employee_id>")
# def employee_detail(employee_id):
#     return f"Employee ID: {employee_id}"

# Get
# @app.route("/employees", methods=["GET"])
# def get_employees():
#     return "Getting all employees"

# Post plan response
# @app.route("/employees/add", methods=["POST"])
# def add_employee():

#     data = request.get_json()

#     name = data["name"]
#     salary = data["salary"]

#     return f"Employee {name} with salary {salary} received"

# Post json response
# @app.route("/employees/add", methods=["POST"])
# def add_employee():

#     data = request.get_json()

#     name = data["name"]
#     salary = data["salary"]

#     return {
#         "message": "Employee created successfully",
#         "name": name,
#         "salary": salary
#     }

# Post database response
@app.route("/employees/add", methods=["POST"])
def add_employee():

    data = request.get_json()

    name = data["name"]
    salary = data["salary"]

    connection = get_connection()
    cursor = connection.cursor()

    query = """
    INSERT INTO employees (name, salary)
    VALUES (%s, %s)
    """

    cursor.execute(query, (name, salary))

    connection.commit()

    cursor.close()
    connection.close()

    return {
        "message": "Employee saved successfully",
        "name": name,
        "salary": salary
    }

# Get database response
@app.route("/employees", methods=["GET"])
def get_all_employees():

    connection = get_connection()
    cursor = connection.cursor(dictionary=True)

    cursor.execute("SELECT * FROM employees")

    employees = cursor.fetchall()

    cursor.close()
    connection.close()

    return employees

# Get database response with id
@app.route("/employees/<int:employee_id>", methods=["GET"])
def get_employee(employee_id):

    connection = get_connection()
    cursor = connection.cursor(dictionary=True)

    query = "SELECT * FROM employees WHERE id = %s"

    cursor.execute(query, (employee_id,))

    employee = cursor.fetchone()

    cursor.close()
    connection.close()

    return employee

# Put database response update
@app.route("/employees/<int:employee_id>", methods=["PUT"])
def update_employee(employee_id):

    data = request.get_json()

    name = data["name"]
    salary = data["salary"]

    connection = get_connection()
    cursor = connection.cursor()

    query = """
    UPDATE employees
    SET name = %s, salary = %s
    WHERE id = %s
    """

    cursor.execute(query, (name, salary, employee_id))

    connection.commit()

    cursor.close()
    connection.close()

    return {
        "message": "Employee updated successfully"
    }

# Delete database response
@app.route("/employees/<int:employee_id>", methods=["DELETE"])
def delete_employee(employee_id):

    connection = get_connection()
    cursor = connection.cursor()

    query = """
    DELETE FROM employees
    WHERE id = %s
    """

    cursor.execute(query, (employee_id,))

    connection.commit()

    cursor.close()
    connection.close()

    return {
        "message": "Employee deleted successfully"
    }

if __name__ == "__main__":
    app.run(debug=True)