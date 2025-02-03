import numpy as np

# 1. From a List
array_from_list = np.array([1, 2, 3, 4, 5])
print("Array from list:", array_from_list)

# 2. Using numpy.zeros
array_zeros = np.zeros((3, 4))  # 3 rows, 4 columns
print("Array of zeros:\n", array_zeros)

# 3. Using numpy.ones
array_ones = np.ones((2, 4))  # 2 rows, 4 columns
print("Array of ones:\n", array_ones)

# 4. Using numpy.arange
array_range = np.arange(0, 10, 2)  # Start: 0, Stop: 10 (exclusive), Step: 2
print("Array using a range:", array_range)