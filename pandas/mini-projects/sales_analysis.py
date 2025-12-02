import pandas as pd

# Sample sales data
df = pd.DataFrame({
    "product": ["A", "B", "A", "C", "B", "A"],
    "quantity": [3, 5, 2, 8, 4, 6],
    "price": [100, 200, 100, 150, 200, 100]
})

df["total"] = df["quantity"] * df["price"]

print("Sales Data:\n", df)

# Total revenue per product
revenue = df.groupby("product")["total"].sum()
print("\nRevenue per product:\n", revenue)

# Best selling product
best = df.groupby("product")["quantity"].sum().idxmax()
print("\nBest selling product:", best)
