import pandas as pd

df = pd.read_csv(
    r"C:\Development\python\data_science\dataset\titanic.csv"
)

df = df.rename(columns={
    "Sex": "Gender",
    "Fare": "Ticket_Fare"
})

print(df.head())
print("\nColumns:")
print(df.columns)