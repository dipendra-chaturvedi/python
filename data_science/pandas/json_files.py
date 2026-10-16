import pandas as pd

df = pd.read_csv(
    r"C:\Development\python\data_science\dataset\titanic.csv"
)

df.head().to_json(
    r"C:\Development\python\data_science\dataset\titanic_sample.json",
    orient="records",
    indent=4
)

json_df = pd.read_json(
    r"C:\Development\python\data_science\dataset\titanic_sample.json"
)

print(json_df)