from sklearn.datasets import load_iris
iris= load_iris()
X=iris.data
y=iris.target
feature_names= iris.feature_names
target_names=iris.feature_names
print("feature names:",feature_names)
print("target names:",target_names)
print("/n first 10 rows of x;/nm",X[:10])