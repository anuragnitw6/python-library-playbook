import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("Salary_dataset.csv")

sample = df.head(10)
plt.scatter(sample["YearsExperience"], sample["Salary"])
plt.title("Mini Scatter Plot (First 10 Rows)")
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.show()
