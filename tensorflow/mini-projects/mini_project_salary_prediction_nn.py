import pandas as pd
import tensorflow as tf
import numpy as np

df = pd.read_csv("Salary_dataset.csv")

X = df[["yearsExperience"]].values
y = df["salary"].values

model = tf.keras.Sequential([
    tf.keras.layers.Dense(32, activation='relu'),
    tf.keras.layers.Dense(32, activation='relu'),
    tf.keras.layers.Dense(1)
])

model.compile(optimizer="adam", loss="mse")
model.fit(X, y, epochs=500, verbose=0)

model.save("salary_nn_model.h5")

exp = 7
pred = model.predict(np.array([[exp]]))[0][0]
print(f"Predicted Salary for {exp} years: ₹{pred:,.2f}")
