import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

matrix = np.random.rand(5, 5)

sns.heatmap(matrix, annot=True)
plt.title("Mini Heatmap (5x5)")
plt.show()
