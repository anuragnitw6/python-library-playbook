import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print("a + b =", a + b)
print("a - b =", a - b)
print("a * b =", a * b)
print("a / b =", a / b)

# Scalar operations
print("a * 10 =", a * 10)

# Dot product
dot = np.dot(a, b)
print("Dot Product:", dot)

# Broadcasting
matrix = np.array([[1, 2, 3], [4, 5, 6]])
broadcasted = matrix + 5
print("Broadcasted Matrix:\n", broadcasted)
