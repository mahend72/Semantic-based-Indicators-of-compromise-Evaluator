# Semantic-based-Indicators-of-compromise-Evaluator: User Guide

## Installation

### Pre-requisites

#### Software

- [Python](https://www.python.org/downloads/) (required)

- [OTXv2](https://pypi.org/project/OTXv2/)

  OTXv2 is an API client library for accessing the Open Threat Exchange, a collaborative platform that allows cybersecurity professionals to share and access threat intelligence data.
  ```bash
  pip install OTXv2

- [tensorflow](https://github.com/tensorflow/tensorflow)

  TensorFlow is an open-source machine learning library developed by the Google Brain team. It is widely used for building and training machine learning models, particularly deep learning models.  
  ```bash 
  pip install tensorflow


- [tensorflow_hub](https://github.com/tensorflow/hub)

  TensorFlow Hub is a library and platform for reusable machine learning modules. It allows the sharing and reuse of pre-trained models and model components.
  ```bash
  pip install tensorflow_hub

- [sentence-tansformers](https://github.com/UKPLab/sentence-transformers/tree/master/sentence_transformers)

  Sentence Transformers is a library for generating embeddings (vector representations) of sentences. It uses pre-trained models to encode sentences into fixed-size vectors.
  ```bash
  pip install sentence-transformers

- SQLite Library
  ```bash
  sudo apt-get update
  sudo apt-get install sqlite3
  sqlite3 --version
  sqlite3 Secureloan.db #not required

#### Procedure for Installation and Run
- Step 1: Clone the Project
Get the resource file from GitHub by cloning the project:

  ```bash
  git clone https://github.com/mahend72/Semantic-based-Indicators-of-compromise-Evaluator.git

- Step 2: IOC Collection
Gather Indicators of Compromise (IOCs) from various sources such as threat intelligence feeds, logs, or security incidents.

- Step 3: Embedding Generation (Feature Matrix)
Transform IOCs into numerical representations using embedding techniques, creating a feature matrix.

- Step 4: Compute Adjacency Matrix
Based on the nature of your data, establish connections or relationships between data points and create an adjacency matrix.

- Step 5: Generate Relation
Define and create relations between entities or features in the dataset, representing the connections within the data.

- Step 6: Compute Meta-Path and Meta-Graph
Define meta-paths, which are sequences of relations, and create a meta-graph to capture higher-level relationships in the data.

- Step 7: Compute Meta-Path and Meta-Graph Instance Similarity Score
Measure the similarity between instances in the meta-graph based on defined meta-paths, quantifying the relatedness of different entities.

- Step 8: Compute GCN (Graph Convolutional Network)
Apply Graph Convolutional Network techniques to learn and propagate information across the graph structure, capturing complex relationships and enhancing feature representations.



