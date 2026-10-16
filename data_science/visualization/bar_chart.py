import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(
    r"C:\Development\python\data_science\dataset\titanic.csv"
)

df["Sex"].value_counts().plot(
    kind="bar",
    color=["blue", "orange"],
    figsize=(8, 5)
)

plt.title("Male vs Female Passengers")
plt.xlabel("Gender")
plt.ylabel("Passenger Count")
plt.grid(axis="y", linestyle="--", alpha=0.5)
plt.tight_layout()
plt.show()