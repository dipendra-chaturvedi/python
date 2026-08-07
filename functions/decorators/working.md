## A decorator is a function that takes another function, adds extra behavior before or after it, and returns a modified function without changing the original function's code.

## Without Decorator

Call Function
      │
      ▼
delete_employee()
      │
      ▼
Deleted

def home():
    # check login
    # check token
    # check permission
    # write log
    return "Home"


## With Decorator

Call Function
      │
      ▼
wrapper()
      │
      ▼
Check Role
      │
 ┌────┴────┐
 │         │
No        Yes
 │         │
 ▼         ▼
Denied   delete_employee()
              │
              ▼
          Employee Deleted


@login_required
def home():
    return "Home"

@admin_required
def delete_employee():
    ...