import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

df = sns.load_dataset("iris").head(20)

sns.pairplot(df)
plt.show()
