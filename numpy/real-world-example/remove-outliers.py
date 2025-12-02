import numpy as np

data = np.array([10, 12, 13, 14, 1000, 15, 16, 20])

mean = np.mean(data)
std = np.std(data)

threshold = 3
filtered_data = data[np.abs(data - mean) < threshold * std]

print("Original Data:", data)
print("Filtered Data (Outliers Removed):", filtered_data)
