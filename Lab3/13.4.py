import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Sample Data: Create a DataFrame for illustration
data = {
    'Category': ['A', 'B', 'C', 'D', 'E'],
    'Values': [23, 45, 56, 78, 33]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Create a bar plot using seaborn
plt.figure(figsize=(8, 6))
sns.barplot(x='Category', y='Values', data=df, palette='Blues')

# Set the title and labels
plt.title('Bar Plot Example', fontsize=16)
plt.xlabel('Category', fontsize=14)
plt.ylabel('Values', fontsize=14)

# Show the plot
plt.show()
