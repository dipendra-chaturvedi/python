import pandas as pd

df = pd.read_csv(
    r"C:\Development\python\data_science\dataset\titanic.csv"
)

df = df.drop(columns=["Cabin"])

print(df.head())
print("\nColumns:")
print(df.columns)