import pandas as pd

df = pd.read_csv(
    r"C:\Development\python\data_science\dataset\titanic.csv"
)

df["Fare_Doubled"] = df["Fare"].apply(lambda fare: fare * 2)

print(df[["Fare", "Fare_Doubled"]].head())