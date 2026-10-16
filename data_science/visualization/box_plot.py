import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(
    r"C:\Development\python\data_science\dataset\titanic.csv"
)

df.boxplot(column="Age")

plt.title("Passenger Age Distribution")
plt.ylabel("Age")
plt.savefig(
    r"C:\Development\python\data_science\visualization\box_plot.png",
    dpi=300,
    bbox_inches="tight"
)
plt.show()