import numpy as np

# Create a sample 1D array
array = np.arange(1, 13)  # Create an array from 1 to 12
print("Original 1D Array:", array)

# 1. Reshaping the array
reshaped_array = array.reshape(3, 4)  # Reshape to 3 rows, 4 columns
print("\nReshaped Array (3x4):\n", reshaped_array)

# 2. Transposing the reshaped array
transposed_array = reshaped_array.T  # Transpose the array
print("\nTransposed Array (4x3):\n", transposed_array)

# 3. Reshape to another shape
reshaped_2d_to_1d = reshaped_array.reshape(-1)  # Reshape back to 1D
print("\nReshaped Back to 1D Array:", reshaped_2d_to_1d)

# 4. Reshaping to higher dimensions
reshaped_to_3d = array.reshape(2, 2, 3)  # Reshape to 3D (2x2x3)
print("\nReshaped to 3D Array (2x2x3):\n", reshaped_to_3d)

# 5. Transposing a 3D array
transposed_3d = np.transpose(reshaped_to_3d, (1, 0, 2))  # Swap axes
print("\nTransposed 3D Array (axes swapped):\n", transposed_3d)