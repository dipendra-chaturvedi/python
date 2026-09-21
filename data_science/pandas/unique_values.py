import pandas as pd

df = pd.read_csv(
    r"C:\Development\python\data_science\dataset\titanic.csv"
)

print("Unique values:")
print(df["Pclass"].unique())

print("\nNumber of unique values:")
print(df["Pclass"].nunique())