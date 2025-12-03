import pandas as pd
from sklearn.linear_model import LinearRegression

# Load data
df = pd.read_csv("Salary_dataset.csv")

# Feature and target
X = df[["yearsExperience"]]
y = df["salary"]

# Train model
model = LinearRegression()
model.fit(X, y)

print("Coefficient:", model.coef_[0])
print("Intercept:", model.intercept_)

exp = 5
pred = model.predict([[exp]])[0]
print(f"Predicted Salary for {exp} years experience: ₹{pred:,.2f}")
