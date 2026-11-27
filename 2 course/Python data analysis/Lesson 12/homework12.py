import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

data = {
    "category": [
        "Електроніка",
        "Одяг",
        "Одяг",
        "Електроніка",
        "Дім",
        "Дім",
        "Одяг",
    ],
    "amount": [12000.0, 1500.0, None, 8500.0, 3200.0, None, 2100.0],
}
df = pd.DataFrame(data)

print(df.isna().sum())

df["amount"] = df["amount"].fillna(df["amount"].median())

summary = df.groupby("category")["amount"].sum().reset_index()
print(summary)

plt.figure(figsize=(8, 5))
sns.set_style("whitegrid")
sns.barplot(data=summary, x="category", y="amount", color="maroon")
plt.title("Сумарний виторг за категоріями")
plt.xlabel("Категорія")
plt.ylabel("Сумарний виторг")
plt.savefig("sales_summary.png", dpi=150, bbox_inches="tight")
plt.show()
plt.close()