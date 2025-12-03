import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

df = pd.read_csv("Salary_dataset.csv")

# Create target classes
df["salary_level"] = pd.qcut(df["salary"], q=3, labels=["Low", "Medium", "High"])

X = df[["yearsExperience"]]
y = df["salary_level"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model
clf = RandomForestClassifier()
clf.fit(X_train, y_train)

accuracy = clf.score(X_test, y_test)
print("Model Accuracy:", accuracy)

exp = 4
pred = clf.predict([[exp]])[0]
print(f"Salary Class for {exp} years experience: {pred}")
