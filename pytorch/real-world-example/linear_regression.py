import torch
import pandas as pd

df = pd.read_csv("Salary_dataset.csv")
X = torch.tensor(df["yearsExperience"].values, dtype=torch.float32).reshape(-1,1)
y = torch.tensor(df["salary"].values, dtype=torch.float32).reshape(-1,1)

# Model
model = torch.nn.Linear(1, 1)

# Loss + Optimizer
criterion = torch.nn.MSELoss()
optimizer = torch.optim.SGD(model.parameters(), lr=0.001)

# Train
for epoch in range(500):
    optimizer.zero_grad()
    y_pred = model(X)
    loss = criterion(y_pred, y)
    loss.backward()
    optimizer.step()

exp = torch.tensor([[5.0]])
pred = model(exp).item()

print(f"Predicted Salary: ₹{pred:,.2f}")
