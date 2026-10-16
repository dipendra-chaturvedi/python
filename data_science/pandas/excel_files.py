import pandas as pd

df = pd.read_csv(
    r"C:\Development\python\data_science\dataset\titanic.csv"
)

df.head().to_excel(
    r"C:\Development\python\data_science\dataset\titanic_sample.xlsx",
    index=False
)

excel_df = pd.read_excel(
    r"C:\Development\python\data_science\dataset\titanic_sample.xlsx"
)

print(excel_df)