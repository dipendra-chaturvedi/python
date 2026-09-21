import pandas as pd

data = {
    "Name": ["Dipendra", "Rahul", "Amit", "Priya"],
    "Salary": [60000, 55000, 70000, 65000],
    "Department": ["IT", "HR", "IT", "HR"]
}

df = pd.DataFrame(data)

result = df.groupby("Department")["Salary"].mean()

print(result)