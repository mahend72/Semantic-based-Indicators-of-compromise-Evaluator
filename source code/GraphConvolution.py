import torch
import torch.nn as nn
import torch.nn.functional as F
import numpy as np
import pandas as pd

#adjacency_matrix = np.random.rand(266, 266)  # Example random adjacency matrix
#feature_matrix = np.random.rand(266, 32)  # Example random feature matrix

adjacency_matrix = MIIS

adj = torch.tensor(adjacency_matrix, dtype=torch.float32)
feature_matrix = feature_matrix.apply(pd.to_numeric, errors='coerce')

# Convert feature_matrix to a PyTorch tensor.
feature_tensor = torch.tensor(feature_matrix.values, dtype=torch.float32)

class GraphConvolution(nn.Module):
    def __init__(self, in_features, out_features):
        super().__init__()
        self.in_features = in_features
        self.out_features = out_features

        self.W = nn.Linear(in_features, out_features)

    def forward(self, input: torch.Tensor, adj: torch.Tensor) -> torch.Tensor:
        support = torch.mm(adj, input)  # Perform matrix multiplication between adjacency matrix and input features
        output = self.W(support)  # Apply linear transformation
        return output

# Create an instance of the GraphConvolution class.
gcn = GraphConvolution(32, 32)

# Pass the input data to the forward method.
output = gcn(feature_tensor, adj)
print(output)

aggregated_output = torch.mean(output, dim=1)

# Print the aggregated output
print(aggregated_output)