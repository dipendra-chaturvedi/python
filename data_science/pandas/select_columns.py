import pandas as pd

data = {
    "Name": ["Dipendra", "Rahul", "Amit"],
    "Salary": [60000, 55000, 70000],
    "Department": ["IT", "HR", "IT"]
}

df = pd.DataFrame(data)

print(df["Name"])
print(df["Salary"])
print(df["Department"])