import pandas as pd

data = {
    "Name": ["Dipendra", "Rahul", "Amit"],
    "Salary": [60000, 55000, 70000],
    "Department": ["IT", "HR", "IT"]
}

df = pd.DataFrame(data)

print(df.iloc[0])
print(df.iloc[1:3])