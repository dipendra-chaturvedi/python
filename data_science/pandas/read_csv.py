import pandas as pd

df = pd.read_csv(
    r"C:\Development\python\data_science\dataset\titanic.csv"
)

print(df.head())

print("\nDataset Information:")
df.info()

print("\nStatistical Summary:")
print(df.describe())

print("\nDataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns)

print("\nAge Column:")
print(df["Age"])

print("\nSelected Columns:")
print(df[["Name", "Age", "Fare"]])

print("\nPassengers older than 50:")
print(df[df["Age"] > 50])