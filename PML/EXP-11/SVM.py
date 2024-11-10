import numpy as np
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix, accuracy_score
dataset = load_digits()
x_train, x_test, y_train, y_test = train_test_split(dataset.data, dataset.target, test_size=0.30,
random_state=4)
Classifier = SVC(kernel="linear")
Classifier.fit(x_train, y_train)
y_pred = Classifier.predict(x_test)
accuracy = accuracy_score(y_test,y_pred)*100
confusion_mat = confusion_matrix(y_test,y_pred)
print("Accuracy for SVM is:",accuracy)
print("Confusion Matrix")
print(confusion_mat)
