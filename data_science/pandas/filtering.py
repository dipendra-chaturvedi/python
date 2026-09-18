import pandas as pd

data = {
    "Name": ["Dipendra", "Rahul", "Amit"],
    "Salary": [60000, 55000, 70000],
    "Department": ["IT", "HR", "IT"]
}

df = pd.DataFrame(data)

high_salary = df[df["Salary"] > 60000]
low_salary = df[df["Salary"] <= 60000]

print(high_salary)
print(low_salary)