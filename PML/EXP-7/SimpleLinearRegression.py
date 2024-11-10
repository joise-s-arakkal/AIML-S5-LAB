import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

data = pd.read_csv("train_data.csv")

X = data['YearsExperience'].values.reshape(-1,1)
Y = data['Salary'].values

model = LinearRegression()
model.fit(X,Y)
Y_pred = model.predict(X)

mse = mean_squared_error(Y,Y_pred)
r2 = r2_score(Y,Y_pred)

plt.scatter(X,Y,label = "Data")
plt.plot(X,Y_pred,color = 'red',label='Regression Line')
plt.xlabel('YearsExperience')
plt.ylabel('Salary')
plt.title("Simple Linear Regression")
plt.legend()
plt.show()

print(f"Mean Squared Error: {mse}")
print(f"R-Squared Error: {r2}")
