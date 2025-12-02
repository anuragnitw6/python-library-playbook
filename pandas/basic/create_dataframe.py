import pandas as pd

# Creating DataFrame from dictionary
data = {
    "name": ["Alice", "Bob", "Charlie"],
    "age": [24, 30, 29],
    "salary": [50000, 62000, 58000]
}

df = pd.DataFrame(data)
print("DataFrame:\n", df)

# Basic info
print("\nInfo:")
print(df.info())

# Describe statistics
print("\nStatistics:")
print(df.describe())
