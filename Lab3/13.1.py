import matplotlib.pyplot as plt
import numpy as np

# Sample data
x = np.linspace(0, 10, 100)  # 100 points from 0 to 10
y = np.sin(x)

# Plot
plt.figure(figsize=(8, 5))
plt.plot(x, y, label="sin(x)", color="blue", linestyle="--")

# Add labels, title, and legend
plt.title("Sine Wave", fontsize=14)
plt.xlabel("X-axis (Values)", fontsize=12)
plt.ylabel("Y-axis (sin(x))", fontsize=12)
plt.legend()
plt.grid(True)

# Show plot
plt.show()