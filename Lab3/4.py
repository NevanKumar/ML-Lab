import numpy as np
from scipy import stats  # Required for mode calculation

# Create a sample array
data = np.array([1, 2, 2, 3, 4, 4, 4, 5, 6])

print("Data Array:", data)

# 1. Mean
mean_value = np.mean(data)
print("Mean:", mean_value)

# 2. Median
median_value = np.median(data)
print("Median:", median_value)

# 3. Mode
mode_value, mode_count = stats.mode(data, keepdims=True)  # Use scipy.stats for mode
print("Mode:", mode_value[0], "Count:", mode_count[0])