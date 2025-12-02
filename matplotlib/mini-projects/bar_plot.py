import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("Salary_dataset.csv")
first_10 = df.head(10)

plt.bar(first_10["YearsExperience"], first_10["Salary"])
plt.title("Salary Bar Chart (First 10 Rows)")
plt.xlabel("Years Experience")
plt.ylabel("Salary")
plt.show()
