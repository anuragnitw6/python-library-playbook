import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("Salary_dataset.csv")

X = df[["yearsExperience"]]
y = df["salary"]

model = LinearRegression()
model.fit(X, y)

# Predictions
y_pred = model.predict(X)

# Plot
plt.scatter(X, y, label="Actual")
plt.plot(X, y_pred, label="Regression Line")
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.title("Salary Prediction Regression Model")
plt.legend()
plt.show()
