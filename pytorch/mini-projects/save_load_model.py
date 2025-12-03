import torch
import torch.nn as nn

model = nn.Linear(1, 1)
torch.save(model.state_dict(), "model.pth")

loaded = nn.Linear(1, 1)
loaded.load_state_dict(torch.load("model.pth"))

print("Model saved and loaded successfully!")
