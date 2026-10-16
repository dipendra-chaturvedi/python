import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(
    r"C:\Development\python\data_science\dataset\titanic.csv"
)

df["Age"].dropna().plot(kind="hist", bins=20)

plt.title("Passenger Age Distribution")
plt.xlabel("Age")
plt.ylabel("Number of Passengers")
plt.show()