import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(
    r"C:\Development\python\data_science\dataset\titanic.csv"
)

survival_counts = df["Survived"].value_counts().sort_index()

plt.pie(
    survival_counts,
    labels=["Did Not Survive", "Survived"],
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Titanic Passenger Survival Rate")

plt.savefig(
    r"C:\Development\python\data_science\visualization\pie_chart.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()