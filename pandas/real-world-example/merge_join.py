import pandas as pd

employees = pd.DataFrame({
    "id": [1, 2, 3],
    "name": ["Alice", "Bob", "Charlie"]
})

salaries = pd.DataFrame({
    "id": [1, 2, 3],
    "salary": [50000, 60000, 70000]
})

merged = pd.merge(employees, salaries, on="id")
print("Merged DataFrame:\n", merged)
