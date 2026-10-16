import pandas as pd

employees_1 = pd.DataFrame({
    "Name": ["Dipendra", "Rahul"],
    "Salary": [60000, 55000]
})

employees_2 = pd.DataFrame({
    "Name": ["Amit", "Priya"],
    "Salary": [70000, 65000]
})

result = pd.concat(
    [employees_1, employees_2],
    ignore_index=True
)

print(result)