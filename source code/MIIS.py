def compute_miis(path_list):
    m = [[0 for col in range(len(path_list[0]))] for row in range(len(path_list[0]))]
    for i in range(len(path_list[0])):
      for j in range(len(path_list[0][0])):
        for k in range(len(path_list)):
            miis= 0
            num_p_ii = path_list[k][i][i]
            num_p_jj = path_list[k][j][j]
            num_p_ij =path_list[k][i][j]
            if num_p_ii == 0 or num_p_jj == 0:
                continue
            miis += (2 * num_p_ij) / (num_p_ii + num_p_jj)
        m[i][j]=miis
    #print("m", m)
    return m
	
MIIS= compute_miis(path_list)
print("miis", MIIS)