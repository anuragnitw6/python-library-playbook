import numpy as np

X = np.random.rand(4, 3)  # Input features
W = np.random.rand(3, 2)  # Weights

y_pred = np.dot(X, W)

print("Input Matrix (X):\n", X)
print("Weights (W):\n", W)
print("Output (XW):\n", y_pred)
