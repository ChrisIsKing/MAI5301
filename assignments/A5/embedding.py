import torch
import torch.nn as nn

class Embedding(nn.Module):
    def __init__(self, num_entries, dim):
        super().__init__()
        self.weight = nn.Parameter(torch.randn(num_entries, dim))

    def forward(self, indices):
        return self.weight[indices]