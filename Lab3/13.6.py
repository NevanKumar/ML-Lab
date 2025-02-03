import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Sample Data: Generate random data for illustration
data = np.random.randn(100)  # 100 random numbers from a normal distribution

# Create a box plot using seaborn
plt.figure(figsize=(8, 6))
sns.boxplot(data=data, color='lightgreen')

# Set the title and labels
plt.title('Box Plot Example', fontsize=16)
plt.xlabel('Category', fontsize=14)
plt.ylabel('Value', fontsize=14)

# Show the plot
plt.show()
