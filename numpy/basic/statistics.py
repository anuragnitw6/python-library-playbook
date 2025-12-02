import numpy as np

data = np.array([10, 20, 30, 40, 50])

print("Mean:", np.mean(data))
print("Median:", np.median(data))
print("Standard Deviation:", np.std(data))
print("Variance:", np.var(data))
print("Min:", np.min(data))
print("Max:", np.max(data))

# Axis-based statistics
matrix = np.array([[1, 2, 3], [4, 5, 6]])

print("Column Means:", np.mean(matrix, axis=0))
print("Row Means:", np.mean(matrix, axis=1))
