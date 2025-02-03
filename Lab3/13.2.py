import matplotlib.pyplot as plt

# Data for the plot
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Create a line plot
plt.plot(x, y, label="y = 2x", color="blue", marker="o")

# Add title and labels
plt.title("Simple Line Plot", fontsize=14)
plt.xlabel("X-axis", fontsize=12)
plt.ylabel("Y-axis", fontsize=12)

# Add legend
plt.legend()

# Display the plot
plt.show()