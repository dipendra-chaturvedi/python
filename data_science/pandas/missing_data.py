import pandas as pd

data = {
    "Name": ["Dipendra", "Rahul", "Amit", "Priya"],
    "Salary": [60000, None, 70000, None],
    "Department": ["IT", "HR", None, "HR"]
}

df = pd.DataFrame(data)

print("Original Data:")
print(df)

print("\nMissing Values:")
print(df.isnull())

print("\nMissing Count:")
print(df.isnull().sum())

df["Salary"] = df["Salary"].fillna(df["Salary"].mean())
df["Department"] = df["Department"].fillna("Unknown")

print("\nAfter Filling Missing Values:")
print(df)


clean_df = df.dropna()

print("\nAfter Removing Missing Rows:")
print(clean_df)