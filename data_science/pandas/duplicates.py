import pandas as pd

data = {
    "Name": ["Dipendra", "Rahul", "Amit", "Rahul"],
    "Salary": [60000, 55000, 70000, 55000],
    "Department": ["IT", "HR", "IT", "HR"]
}

df = pd.DataFrame(data)

print("Duplicate Rows:")
print(df[df.duplicated()])

clean_df = df.drop_duplicates()

print("\nAfter Removing Duplicates:")
print(clean_df)