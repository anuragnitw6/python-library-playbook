import pandas as pd

df = pd.DataFrame({
    "department": ["HR", "HR", "IT", "IT", "Finance"],
    "employee": ["Alice", "Bob", "Charlie", "David", "Eve"],
    "salary": [50000, 55000, 60000, 65000, 70000]
})

grouped = df.groupby("department")["salary"].mean()
print("Average salary per department:\n", grouped)
