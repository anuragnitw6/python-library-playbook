import numpy as np
import time

# Python list
py_list = list(range(1_000_000))
start = time.time()
py_result = [x * 2 for x in py_list]
end = time.time()
print("Python time:", end - start)

# NumPy array
np_arr = np.arange(1_000_000)
start = time.time()
np_result = np_arr * 2
end = time.time()
print("NumPy time:", end - start)
