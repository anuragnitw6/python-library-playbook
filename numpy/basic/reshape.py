import numpy as np

arr = np.arange(12)
print("Original Array:", arr)

reshaped = arr.reshape(3, 4)
print("Reshaped (3x4):\n", reshaped)

flattened = reshaped.flatten()
print("Flattened:", flattened)

# Reshape into 3D
arr3d = np.arange(24).reshape(2, 3, 4)
print("3D Array:\n", arr3d)
