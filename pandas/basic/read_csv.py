import pandas as pd

# Reading CSV
df = pd.read_csv("Sample_dataset.csv")
print("CSV Data:\n", df.head())

# Reading Excel
# df = pd.read_excel("data.xlsx")

# Writing to CSV
df.to_csv("output.csv", index=False)
print("Saved output.csv")
