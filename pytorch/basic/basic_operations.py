import torch

# Create tensors
a = torch.tensor([2, 4, 6])
b = torch.tensor([1, 2, 3])

print("Addition:", a + b)
print("Elementwise Multiply:", a * b)
print("Dot Product:", torch.dot(a, b))
print("Matrix Multiply:", torch.matmul(a, b))
