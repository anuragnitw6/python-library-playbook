import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Salary_dataset.csv")

sns.regplot(x="YearsExperience", y="Salary", data=df)
plt.title("Salary vs Experience (Regression Line)")
plt.show()
