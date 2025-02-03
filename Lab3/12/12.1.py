import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

# Load the CSV file into a pandas DataFrame
file_path = '/mnt/data/Iris.csv'
iris_df = pd.read_csv(file_path)

# 1. Explore Basic DataFrame Operations
print("First 5 rows of the DataFrame:")
print(iris_df.head())

print("\nLast 5 rows of the DataFrame:")
print(iris_df.tail())

print("\nGeneral information about the DataFrame:")
print(iris_df.info())

print("\nSummary statistics of the numeric columns:")
print(iris_df.describe())

# 2. Selecting and Indexing Data
print("\nSelecting a single column (Species):")
print(iris_df['Species'].head())

print("\nSelecting multiple columns (SepalLengthCm and Species):")
print(iris_df[['SepalLengthCm', 'Species']].head())

print("\nSelecting rows by index (first 5 rows):")
print(iris_df.iloc[0:5])

# 3. Filtering Data Based on Conditions
print("\nFiltering rows where SepalLengthCm > 5.0:")
filtered_df = iris_df[iris_df['SepalLengthCm'] > 5.0]
print(filtered_df)

# 4. Basic Data Cleaning
# Checking for missing values
print("\nChecking for missing values in each column:")
print(iris_df.isnull().sum())

# Fill missing values with column mean (if any)
iris_df = iris_df.fillna(iris_df.mean(numeric_only=True))
print("\nDataFrame after handling missing values (if any were present):")
print(iris_df.head())

# 5. Grouping and Aggregating Data
print("\nMean of numeric columns grouped by Species:")
grouped_mean = iris_df.groupby('Species').mean()
print(grouped_mean)

# 6. Basic Data Visualization
print("\nVisualizing SepalLengthCm distribution by Species:")

# Boxplot for SepalLengthCm by Species
iris_df.boxplot(column='SepalLengthCm', by='Species', grid=False)
plt.title("Sepal Length by Species")
plt.suptitle("")  # Remove the default Pandas plot title
plt.xlabel("Species")
plt.ylabel("Sepal Length (cm)")
plt.show()
