import pandas as pd
import tensorflow as tf

df = pd.read_csv("Salary_dataset.csv")

X = df[["yearsExperience"]].values
y = df["salary"].values

model = tf.keras.Sequential([
    tf.keras.layers.Dense(8, activation='relu'),
    tf.keras.layers.Dense(8, activation='relu'),
    tf.keras.layers.Dense(1)
])

model.compile(optimizer='adam', loss='mse')
model.fit(X, y, epochs=300, verbose=0)

exp = 5
print("Predicted salary:", model.predict([[exp]])[0][0])
