import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report

diabates = load_diabetes()

X,y = diabates.data, diabates.target


y_binary = (y > np.median(y)).astype(int)

X_train, X_test, y_train, y_test = train_test_split(X,y_binary,test_size = 0.2, random_state = 42)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

model = LogisticRegression()
model.fit(X_train,y_train)

y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test,y_pred)
print("Accuracy:{:.2f}%".format(accuracy*100))

print("Confusion Matrix:\n",confusion_matrix(y_test,y_pred))

print("Classification report:\n",classification_report(y_test,y_pred))

plt.figure(figsize = (8,6))
sns.scatterplot(x=X_test[:,2],y=X_test[:,8],hue=y_test,palette={0:'green',1:'red'},marker='*')
plt.xlabel("BMI")
plt.ylabel("Age")
plt.legend()
plt.show()
