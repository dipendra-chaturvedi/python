def admin_required(func):

    def wrapper(role, employee_id):
        if role != "admin":
            print("Access Denied")
            return
        return func(role, employee_id)
    return wrapper

@admin_required
def delete_employee(role, employee_id):
    print(f"Employee {employee_id} deleted successfully")

delete_employee("admin", 101)
delete_employee("user", 102)

