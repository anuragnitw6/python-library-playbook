import seaborn as sns
import matplotlib.pyplot as plt

sns.histplot([10, 20, 20, 40, 50, 50, 60], kde=True)
plt.title("Basic Histogram with KDE")
plt.show()
