import networkx as nx
import torch
import numpy as np

# Example GCN output
gcn_output = output

# Convert tensor to a regular NumPy array

gcn_output = gcn_output.detach().numpy()

# Create a graph from the GCN output
G = nx.Graph()
num_nodes = len(gcn_output)
G.add_nodes_from(range(1, num_nodes + 1))

# Add edges based on GCN output
for i in range(num_nodes):
    for j in range(i + 1, num_nodes):
        if np.greater(gcn_output[i], gcn_output[j]):
            G.add_edge(i + 1, j + 1)

# Calculate the degree centrality of nodes
degree_centrality = nx.degree_centrality(G)

# Print the degree centrality of each node
for node, centrality in degree_centrality.items():
    print(f"Node {node}: Degree Centrality = {centrality}")