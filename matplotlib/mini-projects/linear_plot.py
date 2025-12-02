import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("Salary_dataset.csv")

df_sorted = df.sort_values("YearsExperience")

plt.plot(df_sorted["YearsExperience"], df_sorted["Salary"])
plt.title("Salary Trend by Experience")
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.show()
