import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Sample Data: Generate random data for illustration
data = np.random.randn(1000)  # 1000 random numbers from a normal distribution

# Create a histogram using seaborn
plt.figure(figsize=(8, 6))
sns.histplot(data, kde=True, color='skyblue', bins=30)  # kde=True adds a KDE (Kernel Density Estimate)

# Set the title and labels
plt.title('Histogram with Seaborn', fontsize=16)
plt.xlabel('Value', fontsize=14)
plt.ylabel('Frequency', fontsize=14)

# Show the plot
plt.show()
