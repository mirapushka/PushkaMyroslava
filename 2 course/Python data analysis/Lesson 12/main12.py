import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

np.random.seed(42)
customers = ["Ігор", "Анна", "Дмитро", "Марія", "Олександр", "Олена"]

df = pd.DataFrame({
    "customer": np.random.choice(customers, 100),
    "quantity": np.random.randint(1, 6, 100).astype(float),
    "sales": np.random.randint(200, 5000, 100).astype(float),
})

df.loc[[5, 15, 25], "quantity"] = np.nan
df.loc[[10, 20, 30], "sales"] = np.nan
df.loc[[3, 18], "sales"] = -500.0

df = pd.concat([df, df.iloc[[0, 1, 2]]], ignore_index=True)

print(df.info())
print(df.describe())

df = df.drop_duplicates()
df["quantity"] = df["quantity"].fillna(df["quantity"].median())
df["sales"] = df["sales"].fillna(df["sales"].median())
df = df[df["sales"] >= 0].copy()

summary = df.groupby("customer")["sales"].agg(
    total_sales="sum",
    avg_check="mean",
    orders_count="count"
).reset_index()

print(summary)

plt.figure(figsize=(10, 6))
sns.set_style("whitegrid")
sns.barplot(data=summary, x="customer", y="total_sales", color="maroon")
plt.title("Total Sales by Customer")
plt.xlabel("Customer")
plt.ylabel("Total Sales")
plt.savefig("total_sales_by_customer.png", dpi=150)
plt.show()
plt.close()