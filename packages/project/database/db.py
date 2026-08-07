# import mysql.connector
from database.connection import get_connection

def save_employee(employee):

    connection = get_connection()

    cursor = connection.cursor()

    query = """
    INSERT INTO employees (name, salary)
    VALUES (%s, %s)
    """

    values = (
        employee.name,
        employee.salary
    )

    cursor.execute(query, values)

    connection.commit()

    cursor.close()
    connection.close()

def get_employees():

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("SELECT * FROM employees")

    employees = cursor.fetchall()

    cursor.close()
    connection.close()

    return employees

def update_employee_salary(employee_id, new_salary):

    connection = get_connection()

    cursor = connection.cursor()

    query = """
    UPDATE employees
    SET salary = %s
    WHERE id = %s
    """

    values = (
        new_salary,
        employee_id
    )

    cursor.execute(query, values)

    connection.commit()

    print("Salary Updated Successfully")

    cursor.close()
    connection.close()

def delete_employee(employee_id):

    connection = get_connection()

    cursor = connection.cursor()

    query = """
    DELETE FROM employees
    WHERE id = %s
    """

    cursor.execute(query, (employee_id,))

    connection.commit()

    print("Employee Deleted Successfully")

    cursor.close()
    connection.close()