import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np
import joblib

# Load data
df = pd.read_csv("Salary_dataset.csv")

X = df[["yearsExperience"]]
y = df["salary"]

# Train model
model = LinearRegression()
model.fit(X, y)

# Save model
joblib.dump(model, "salary_model.pkl")
print("Model saved as salary_model.pkl")

# Test
exp = 7
pred = model.predict(np.array(exp).reshape(-1, 1))[0]
print(f"Predicted salary for {exp} years: ₹{pred:,.2f}")
