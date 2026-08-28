from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from database import get_connection
from decorators import login_required

employee_bp = Blueprint(
    "employee",
    __name__
)


@employee_bp.route("/employee")
@login_required
def employee():

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM employees")

    employees = cursor.fetchall()

    cursor.close()
    connection.close()

    return render_template(
        "employee.html",
        employees=employees
    )


@employee_bp.route("/employee/add", methods=["GET", "POST"])
@login_required
def add_employee():

    if request.method == "POST":

        name = request.form.get("name")
        salary = request.form.get("salary")

        connection = get_connection()
        cursor = connection.cursor()

        query = """
        INSERT INTO employees (name, salary)
        VALUES (%s, %s)
        """

        cursor.execute(
            query,
            (name, salary)
        )

        connection.commit()

        cursor.close()
        connection.close()

        flash("Employee added successfully")

        return redirect(
            url_for("employee.employee")
        )
        
    return render_template("add_employee.html")

@employee_bp.route("/employee/<int:id>")
@login_required
def employee_detail(id):

    connection = get_connection()
    cursor = connection.cursor()

    query = """
    SELECT * FROM employees
    WHERE id = %s
    """

    cursor.execute(query, (id,))

    employee = cursor.fetchone()

    cursor.close()
    connection.close()

    if not employee:
        return "Employee not found", 404

    return render_template(
        "employee_detail.html",
        employee=employee
    )

@employee_bp.route("/employee/<int:id>/edit", methods=["GET", "POST"])
@login_required
def edit_employee(id):

    connection = get_connection()
    cursor = connection.cursor()

    if request.method == "POST":

        name = request.form.get("name")
        salary = request.form.get("salary")

        query = """
        UPDATE employees
        SET name = %s,
            salary = %s
        WHERE id = %s
        """

        cursor.execute(
            query,
            (name, salary, id)
        )

        connection.commit()

        cursor.close()
        connection.close()

        flash("Employee updated successfully")

        return redirect(
            url_for("employee.employee")
        )

    query = """
    SELECT * FROM employees
    WHERE id = %s
    """

    cursor.execute(query, (id,))

    employee = cursor.fetchone()

    cursor.close()
    connection.close()

    if not employee:
        return "Employee not found", 404

    return render_template(
        "edit_employee.html",
        employee=employee
    )

@employee_bp.route("/employee/<int:id>/delete", methods=["POST"])
@login_required
def delete_employee(id):

    connection = get_connection()
    cursor = connection.cursor()

    query = """
    DELETE FROM employees
    WHERE id = %s
    """

    cursor.execute(query, (id,))
    connection.commit()

    cursor.close()
    connection.close()

    flash("Employee deleted successfully")

    return redirect(
        url_for("employee.employee")
    )
