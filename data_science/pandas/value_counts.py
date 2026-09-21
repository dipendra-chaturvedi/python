import pandas as pd

df = pd.read_csv(
    r"C:\Development\python\data_science\dataset\titanic.csv"
)

print(df["Sex"].value_counts())