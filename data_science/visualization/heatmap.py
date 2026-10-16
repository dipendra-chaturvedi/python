import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(
    r"C:\Development\python\data_science\dataset\titanic.csv"
)

correlation = df[["Age", "Fare", "SibSp", "Parch", "Pclass"]].corr()

plt.imshow(correlation, cmap="coolwarm", vmin=-1, vmax=1)
plt.colorbar()
plt.xticks(range(len(correlation.columns)), correlation.columns, rotation=45)
plt.yticks(range(len(correlation.columns)), correlation.columns)
plt.title("Titanic Feature Correlation")
plt.tight_layout()

plt.savefig(
    r"C:\Development\python\data_science\visualization\heatmap.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()