import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

data = pd.read_csv("train_data1.csv")

X = data.drop('Y',axis = 1)
Y = data['Y']

model = LinearRegression()
model.fit(X,Y)
Y_pred = model.predict(X)

mse = mean_squared_error(Y,Y_pred)
r2 = r2_score(Y,Y_pred)

print(f"Mean Squared Error: {mse}")
print(f"R-Squared Error: {r2}")

