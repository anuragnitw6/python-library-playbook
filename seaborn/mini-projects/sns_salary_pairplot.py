import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Salary_dataset.csv")

sns.pairplot(df)
plt.suptitle("Pairplot: YearsExperience vs Salary", y=1.02)
plt.show()
