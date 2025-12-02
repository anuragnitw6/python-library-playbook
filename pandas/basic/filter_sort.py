import pandas as pd

df = pd.DataFrame({
    "name": ["Alice", "Bob", "Charlie", "David"],
    "age": [24, 30, 29, 22],
    "salary": [50000, 62000, 58000, 45000]
})

# Filtering
filtered = df[df["age"] > 25]
print("Filtered age > 25:\n", filtered)

# Sorting
sorted_df = df.sort_values(by="salary", ascending=False)
print("\nSorted by salary (desc):\n", sorted_df)

# Selecting columns
selected = df[["name", "salary"]]
print("\nSelected columns:\n", selected)
