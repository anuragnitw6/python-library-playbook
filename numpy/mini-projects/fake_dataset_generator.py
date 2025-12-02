import numpy as np
import pandas as pd

np.random.seed(42)

data = {
    "age": np.random.randint(18, 60, 1000),
    "salary": np.random.normal(50000, 10000, 1000),
    "rating": np.random.uniform(1, 5, 1000),
}

df = pd.DataFrame(data)
df.to_csv("fake_data.csv", index=False)

print("Fake dataset saved as fake_data.csv")
