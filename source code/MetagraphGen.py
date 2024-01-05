import numpy as np


import numpy as np

def num_meta_paths(commuting_matrix, adj_matrix_A, adj_matrix_B, start_node, end_node):
    adj_matrix_A = np.array(adj_matrix_A)
    adj_matrix_B = np.array(adj_matrix_B)
    commuting_matrix = np.array(commuting_matrix)
    num_paths = 0

    indices_A = np.where(adj_matrix_A[:, start_node] > 0)[0]
    indices_B = np.where(adj_matrix_B[:, end_node] > 0)[0]
    commuting_mod = np.arange(commuting_matrix.shape[0]) % commuting_matrix.shape[1]
    for i in indices_A:
        for j in indices_B:
            num_paths += np.sum(
                commuting_matrix[commuting_mod[i%commuting_matrix.shape[1]], commuting_mod[j%commuting_matrix.shape[1]]] *
                adj_matrix_A[i, :] *
                adj_matrix_B[j, :]
            )
    #print("num_path", num_paths)

    return num_paths

def meta_path_list(M,mat):
    meta_path1 = []
    for i in range(len(mat)):
        print("----------------------i", i)
        row_results = []
        for j in range(len(mat)):
            num_paths = num_meta_paths(M, mat, mat, i, j)
            row_results.append(num_paths)
        meta_path1.append(row_results)
    print("meta-path", meta_path1)
    return meta_path1
 
path_list=meta_path_list(M,all_embeddings)
print("list",path_list)