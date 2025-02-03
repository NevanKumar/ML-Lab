import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Sample Data: Generate a 10x10 matrix of random data
data = np.random.rand(10, 10)  # 10x10 matrix with random values

# Create a heatmap using seaborn
plt.figure(figsize=(8, 6))
sns.heatmap(data, cmap='coolwarm', annot=True, fmt=".2f", linewidths=0.5)

# Set the title and labels
plt.title('Heatmap Example', fontsize=16)

# Show the plot
plt.show()
