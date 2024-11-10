import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

data = pd.read_csv("train_data3.csv")

X = data['X'].values.reshape(-1,1)
Y = data['Y'].values

poly = PolynomialFeatures(degree=2)
X_poly = poly.fit_transform(X)

model = LinearRegression()
model.fit(X_poly,Y)

Y_pred = model.predict(X_poly)

X_sort, Y_sort = zip(*sorted(zip(X,Y_pred)))

mse = mean_squared_error(Y,Y_pred)
r2 = r2_score(Y,Y_pred)

plt.scatter(X,Y,label = "Data")
plt.plot(X_sort,Y_sort,color = 'red',label='Polynomial Regression')
plt.xlabel('X')
plt.ylabel('Y')
plt.title("Polynomial Regression")
plt.legend()
plt.show()

print(f"Mean Squared Error: {mse}")
print(f"R-Squared Error: {r2}")
