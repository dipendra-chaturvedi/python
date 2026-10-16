import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(
    r"C:\Development\python\data_science\dataset\titanic.csv"
)

df["Sex"].value_counts().plot(kind="bar")

plt.title("Passenger Count by Gender")
plt.xlabel("Gender")
plt.ylabel("Passenger Count")

plt.savefig(
    r"C:\Development\python\data_science\visualization\gender_chart.png"
)

plt.show()