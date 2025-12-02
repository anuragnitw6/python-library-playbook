import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("Salary_dataset.csv")
plt.hist(df["Salary"], bins=10)
plt.title("Salary Distribution")
plt.xlabel("Salary")
plt.ylabel("Frequency")
plt.show()
