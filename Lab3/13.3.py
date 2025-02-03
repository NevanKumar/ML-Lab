import matplotlib.pyplot as plt
import numpy as np

# Random scatter data
x = np.random.rand(50)
y = np.random.rand(50)

# Scatter plot
plt.figure(figsize=(8, 5))
plt.scatter(x, y, color="green", alpha=0.6)
plt.title("Scatter Plot (Matplotlib)", fontsize=14)
plt.xlabel("X-axis", fontsize=12)
plt.ylabel("Y-axis", fontsize=12)
plt.grid(True)
plt.show()