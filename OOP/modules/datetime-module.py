from datetime import datetime

employee_id = 101

login_time = datetime.now()

print(f"Employee ID : {employee_id}")
print(f"Login Time  : {login_time}")

with open("login_history.txt", "a", encoding="utf-8") as file:
    file.write(f"{employee_id} | {login_time}\n")