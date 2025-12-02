import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Salary_dataset.csv")

corr = df.corr()

sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()
