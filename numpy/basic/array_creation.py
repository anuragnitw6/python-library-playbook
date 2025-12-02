import numpy as np

# Creating 1D array
arr1 = np.array([1, 2, 3, 4, 5])
print("1D Array:", arr1)

# Creating 2D array
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print("2D Array:\n", arr2)

# Create arrays with zeros, ones, and random numbers
zeros_arr = np.zeros((3, 3))
ones_arr = np.ones((2, 4))
random_arr = np.random.rand(3, 3)

print("Zeros Array:\n", zeros_arr)
print("Ones Array:\n", ones_arr)
print("Random Array:\n", random_arr)

# Create range-based arrays
range_arr = np.arange(0, 10, 2)
print("Range Array:", range_arr)

linspace_arr = np.linspace(0, 1, 5)
print("Linspace Array:", linspace_arr)
