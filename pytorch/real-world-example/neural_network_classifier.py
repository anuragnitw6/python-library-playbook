import torch
import torch.nn as nn
import torch.optim as optim
import pandas as pd

df = pd.read_csv("Salary_dataset.csv")

# Create target classes
df["salary_level"] = pd.qcut(df["salary"], 3, labels=[0,1,2])

X = torch.tensor(df["yearsExperience"].values, dtype=torch.float32).reshape(-1,1)
y = torch.tensor(df["salary_level"].values, dtype=torch.long)

class Classifier(nn.Module):
    def __init__(self):
        super().__init__()
        self.layers = nn.Sequential(
            nn.Linear(1, 16),
            nn.ReLU(),
            nn.Linear(16, 3)
        )
    def forward(self, x):
        return self.layers(x)

model = Classifier()
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.01)

for epoch in range(500):
    optimizer.zero_grad()
    out = model(X)
    loss = criterion(out, y)
    loss.backward()
    optimizer.step()

test_exp = torch.tensor([[4.0]])
pred_class = torch.argmax(model(test_exp)).item()
print("Predicted Salary Level:", ["Low","Medium","High"][pred_class])
