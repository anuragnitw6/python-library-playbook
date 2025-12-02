import pandas as pd

df = pd.read_csv("Salary_dataset.csv")

print("Head:\n", df.head())

# Total Salary
total_salary = df["Salary"].sum()
print("\nTotal Salary:", total_salary)

# Top Salaried Employees
top_employees = df.groupby("YearsExperience")["Salary"].sum().sort_values(ascending=False)
print("\nTop Employees:\n", top_employees.head(5))

# Salary growth rate
df["growth_rate"] = df["Salary"].pct_change()
print("\nGrowth Rate:\n", df["growth_rate"])
