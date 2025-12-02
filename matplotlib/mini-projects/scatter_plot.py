import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("Salary_dataset.csv")

plt.figure(figsize=(8,5))
plt.scatter(df["YearsExperience"], df["Salary"])
plt.title("Salary vs Years of Experience")
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.grid(True)
plt.show()
