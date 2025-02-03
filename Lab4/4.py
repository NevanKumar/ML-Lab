import numpy as np
from sklearn import preprocessing
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_digits
print("NEVAN KUMAR")
print("22053791")

digits = load_digits()
digits_x_normalized = preprocessing.normalize(digits.data, norm = 'l1')
digits_y = digits.target

digits_x_train, digits_x_test, digits_y_train, digits_y_test = train_test_split(digits_x_normalized, digits_y, test_size = 0.2, random_state = 42)

from sklearn import svm
classifier = svm.SVC()
classifier.fit(digits_x_train, digits_y_train)
digits_prediction = classifier.predict(digits_x_test)
print(f"Accuracy: {metrics.accuracy_score(digits_y_test, digits_prediction) * 100}%")
