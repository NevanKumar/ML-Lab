from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import Normalizer, StandardScaler
from sklearn.metrics import accuracy_score
from xgboost import XGBClassifier
print("NEVAN KUMAR")
print("22053791")
# Load dataset (Iris dataset as an example)
iris = datasets.load_iris()
X = iris.data
y = iris.target

# Split dataset into training and testing sets
x_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Function to train and evaluate XGBoost model
def train_evaluate_xgb(x_train ,x_test,y_train, y_test):
    model = XGBClassifier(use_label_encoder=False, eval_metric='loss', random_state=42)
    model.fit(x_train, y_train)
    y_predict = model.predict(x_test)
    accuracy = accuracy_score(y_test, y_predict)
    print("Accuracy:", accuracy)
    return accuracy

# 1. Initial XGBoost Training
print("Initial XGBoost Training:")
initial_accuracy = train_evaluate_xgb(x_train, X_test, y_train, y_test)

# 2. Normalize using L1
print("\nAfter L1 Normalization:")
l1_normalizer = Normalizer(norm='l1')
X_train_l1 = l1_normalizer.fit_transform(x_train)
X_test_l1 = l1_normalizer.transform(X_test)
train_evaluate_xgb(X_train_l1, X_test_l1, y_train, y_test)

# 3. Normalize using L2
print("\nAfter L2 Normalization:")
l2_normalizer = Normalizer(norm='l2')
X_train_l2 = l2_normalizer.fit_transform(x_train)
X_test_l2 = l2_normalizer.transform(X_test)
train_evaluate_xgb(X_train_l2, X_test_l2, y_train, y_test)

# 4. Standard Scaling
print("\nAfter Standard Scaling:")
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(x_train)
X_test_scaled = scaler.transform(X_test)
train_evaluate_xgb(X_train_scaled, X_test_scaled, y_train, y_test)
