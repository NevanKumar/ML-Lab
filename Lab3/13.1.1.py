import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Create sample data
data = {
    "Category": ["A", "B", "C", "D"],
    "Values": [15, 30, 45, 10]
}
df = pd.DataFrame(data)

# Barplot
sns.set(style="whitegrid")
plt.figure(figsize=(8, 5))
sns.barplot(x="Category", y="Values", data=df, palette="viridis")

# Add title
plt.title("Bar Plot of Categories", fontsize=14)

plt.show()