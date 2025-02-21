import pandas as pd
import numpy as np
from itertools import product
from sklearn.model_selection import KFold, cross_val_score, cross_validate
from sklearn.svm import SVR
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsRegressor
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.naive_bayes import GaussianNB
from tqdm import tqdm

# Load datasets
red_wine_url = "https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv"
white_wine_url = "https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-white.csv"

red_wine = pd.read_csv(red_wine_url, sep=";")
white_wine = pd.read_csv(white_wine_url, sep=";")

# Split features and target variable
X_red = red_wine.drop('quality', axis=1)
y_red = red_wine['quality']

X_white = white_wine.drop('quality', axis=1)
y_white = white_wine['quality']

# Define models to evaluate
models = {
    'SVR': SVR(),
    'Linear Regression': LinearRegression(),
    'KNN': KNeighborsRegressor(),
    'Random Forest': RandomForestRegressor(),
    'Decision Tree': DecisionTreeRegressor(),
    'Naive Bayes': GaussianNB(),  # Note: GaussianNB is originally for classification.
    'Gradient Boosting': GradientBoostingRegressor()
}

# Cross-validation fold settings to try
cv_folds = [5, 10, 15, 20]


# Function to evaluate a model using cross-validation
# with multiple metrics: MSE, R2, and MAE
def evaluate_model(model, X, y, cv):
    kf = KFold(n_splits=cv, shuffle=True, random_state=42)
    scoring = {
        'mse': 'neg_mean_squared_error',
        'r2': 'r2',
        'mae': 'neg_mean_absolute_error'
    }
    scores = cross_validate(model, X, y, cv=kf, scoring=scoring, n_jobs=-1)
    mse = np.mean(-scores['test_mse'])
    r2 = np.mean(scores['test_r2'])
    mae = np.mean(-scores['test_mae'])
    return mse, r2, mae


# Prepare to store results
results = []
# Create a list of all model and cv combinations using itertools.product
combinations = list(product(models.items(), cv_folds))

# Use tqdm to create a progress bar that tracks the evaluation of all combinations
for (model_name, model), cv in tqdm(combinations, desc="Evaluating models", total=len(combinations)):
    # Evaluate on red wine dataset
    red_mse, red_r2, red_mae = evaluate_model(model, X_red, y_red, cv)
    # Evaluate on white wine dataset
    white_mse, white_r2, white_mae = evaluate_model(model, X_white, y_white, cv)

    results.append({
        'Model': model_name,
        'CV Folds': cv,
        'Red Wine MSE': red_mse,
        'Red Wine R2': red_r2,
        'Red Wine MAE': red_mae,
        'White Wine MSE': white_mse,
        'White Wine R2': white_r2,
        'White Wine MAE': white_mae
    })

results_df = pd.DataFrame(results)
print("Cross-Validation Results:")
print(results_df)

# Find the best model configuration (the one with the lowest MSE) for each dataset
best_red = results_df.loc[results_df['Red Wine MSE'].idxmin()]
best_white = results_df.loc[results_df['White Wine MSE'].idxmin()]

print("\nBest model configuration for Red Wine:")
print(best_red)

print("\nBest model configuration for White Wine:")
print(best_white)