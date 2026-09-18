import pandas as pd

data = {
    "Name": ["Dipendra", "Rahul", "Amit"],
    "Salary": [60000, 55000, 70000],
    "Department": ["IT", "HR", "IT"]
}

df = pd.DataFrame(data)

sorted_df = df.sort_values("Salary", ascending=False)

print(sorted_df)
