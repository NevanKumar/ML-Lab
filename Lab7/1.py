import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Load the Boston dataset manually
data_url = "http://lib.stat.cmu.edu/datasets/boston"
raw_df = pd.read_csv(data_url, sep="\\s+", skiprows=22, header=None)
data = np.hstack([raw_df.values[::2, :], raw_df.values[1::2, :2]])
target = raw_df.values[1::2, 2]

# Create DataFrame
X = pd.DataFrame(data, columns=[
    'CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT'
])
y = pd.Series(target)

# Perform linear regression with a single feature (e.g., RM)
X_single = X[['RM']]
X_train_single, X_test_single, y_train_single, y_test_single = train_test_split(X_single, y, test_size=0.2,
                                                                                random_state=42)

model_single = LinearRegression()
model_single.fit(X_train_single, y_train_single)
y_pred_single = model_single.predict(X_test_single)

mse_single = mean_squared_error(y_test_single, y_pred_single)
print(f"Single Feature Mean Squared Error: {mse_single:.4f}")

# Plot single feature regression
plt.figure(figsize=(10, 6))
plt.scatter(X_test_single, y_test_single, color='blue', label='Actual')
plt.plot(X_test_single, y_pred_single, color='red', linewidth=2, label='Predicted')
plt.xlabel('RM')
plt.ylabel('House Price')
plt.title('Linear Regression with Single Feature (RM)')
plt.legend()
plt.show()

# Perform multiple regression with multiple features
X_train_multi, X_test_multi, y_train_multi, y_test_multi = train_test_split(X, y, test_size=0.2, random_state=42)

model_multi = LinearRegression()
model_multi.fit(X_train_multi, y_train_multi)
y_pred_multi = model_multi.predict(X_test_multi)

mse_multi = mean_squared_error(y_test_multi, y_pred_multi)
print(f"Multiple Features Mean Squared Error: {mse_multi:.4f}")

# Plot multiple feature regression (actual vs predicted)
plt.figure(figsize=(10, 6))
plt.scatter(y_test_multi, y_pred_multi, color='blue', label='Predicted vs Actual')
plt.plot([y_test_multi.min(), y_test_multi.max()], [y_test_multi.min(), y_test_multi.max()], color='red', linewidth=2,
         label='Ideal')
plt.xlabel('Actual House Price')
plt.ylabel('Predicted House Price')
plt.title('Multiple Regression with Multiple Features')
plt.legend()
plt.show()