import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(
    r"C:\Development\python\data_science\dataset\titanic.csv"
)

survived = df[df["Survived"] == 1]["Age"].dropna()
not_survived = df[df["Survived"] == 0]["Age"].dropna()

plt.hist(survived, bins=15, alpha=0.6, label="Survived")
plt.hist(not_survived, bins=15, alpha=0.6, label="Did Not Survive")

plt.title("Passenger Age by Survival")
plt.xlabel("Age")
plt.ylabel("Passenger Count")
plt.legend()
plt.tight_layout()
plt.show()