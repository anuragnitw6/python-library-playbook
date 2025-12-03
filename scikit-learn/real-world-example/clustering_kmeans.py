import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

df = pd.read_csv("Salary_dataset.csv")

X = df[["yearsExperience", "salary"]]

# Apply KMeans
kmeans = KMeans(n_clusters=3)
df["cluster"] = kmeans.fit_predict(X)

# Plot
plt.scatter(df["yearsExperience"], df["salary"], c=df["cluster"])
plt.xlabel("Years Experience")
plt.ylabel("Salary")
plt.title("K-Means Clustering of Salary Data")
plt.show()
