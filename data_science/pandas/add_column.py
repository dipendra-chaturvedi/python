import pandas as pd

data = {
    "Name": ["Dipendra", "Rahul", "Amit"],
    "Salary": [60000, 55000, 70000]
}

df = pd.DataFrame(data)

df["Annual Salary"] = df["Salary"] * 12

print(df)