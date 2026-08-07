from database.db import save_employee
from models.employee import Employee


def register_employee():

    employee = Employee(
        101,
        "Dipendra",
        60000
    )

    save_employee(employee)