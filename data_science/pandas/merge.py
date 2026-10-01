import pandas as pd

employees = pd.DataFrame({
    "EmployeeID": [1, 2, 3],
    "Name": ["Dipendra", "Rahul", "Amit"]
})

salary = pd.DataFrame({
    "EmployeeID": [1, 2, 3],
    "Salary": [60000, 55000, 70000]
})

result = pd.merge(
    employees,
    salary,
    on="EmployeeID"
)

print(result)