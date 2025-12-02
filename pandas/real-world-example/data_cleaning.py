import pandas as pd
import numpy as np

df = pd.DataFrame({
    "name": ["Alice", "Bob", None, "David"],
    "age": [24, None, 29, 22],
    "salary": [50000, 62000, None, 45000]
})

print("Original Data:\n", df)

# Fill missing values
df["age"].fillna(df["age"].mean(), inplace=True)
df["salary"].fillna(df["salary"].median(), inplace=True)
df["name"].fillna("Unknown", inplace=True)

# Remove duplicates
df.drop_duplicates(inplace=True)

print("\nCleaned Data:\n", df)
