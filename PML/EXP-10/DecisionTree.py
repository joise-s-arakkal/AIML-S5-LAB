import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report,confusion_matrix

colnames=['Buying_price', 'maint_cost', 'doors', 'persons','lug_boot','safety','decision']

data = pd.read_csv('car_evaluation.csv', names=colnames, header=None)

plt.figure(figsize=(5,5))
sns.countplot(x='decision',data=data)
plt.title('Count plot for decision')

data.decision.replace('vgood','acc',inplace=True)
data.decision.replace('good','acc',inplace=True)
data['decision'].value_counts()
new_data=data.apply(LabelEncoder().fit_transform)

x=new_data.drop(['decision'], axis=1)
y =new_data['decision']
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.3, random_state = 42)
dt =DecisionTreeClassifier(criterion="entropy")

dt.fit(x_train,y_train)
dt_pred=dt.predict(x_test)
cm=confusion_matrix(y_test,dt_pred)
cm_display = sklearn.metrics.ConfusionMatrixDisplay(confusion_matrix = cm)
cm_display.plot()
plt.show()
