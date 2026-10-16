import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(
    r"C:\Development\python\data_science\dataset\titanic.csv"
)

age_data = df["Age"].dropna().sort_values().reset_index(drop=True)

plt.plot(age_data)

plt.title("Passenger Ages")
plt.xlabel("Passenger Index")
plt.ylabel("Age")
plt.show()