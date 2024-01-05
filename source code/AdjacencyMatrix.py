import numpy as np

#print(hash1)
def com_adj_matrix(file_hash, email_address, ip_address, url_address, domain_address, host_name, region, attack_technique, attacker, cve
,events):

    nodes = file_hash + email_address + ip_address + url_address + domain_address + host_name + region + attack_technique + attacker + cve
    adj_matrix = np.zeros((len(nodes), len(nodes)), dtype=int)
    print("hash", len(file_hash))
    print("email", len(email_address))
    print("ip", len(ip_address))
    print("url", len(url_address))
    print("domain", len(domain_address))
    print("host", len(host_name))
    print("region", len(region))
    print("attack tech", len(attack_technique))
    print("attacker", len(attacker))
    print("cbve", len(cve))
    print(nodes[0] in events[0]["hash"])

    # iterate over each pair of nodes and set the corresponding entry in the adjacency matrix
    for i in range(len(nodes)):
        for j in range(len(nodes)):
          for event in events:
            if nodes[i] in event["hash"] and nodes[j] in event["hash"]:
                adj_matrix[i,j] = 1
            if nodes[i] in event["email"] and nodes[j] in event["email"]:
                adj_matrix[i,j] = 1
            if nodes[i] in event["ip"] and nodes[j] in event["ip"]:
                adj_matrix[i,j] = 1
            if nodes[i] in event["url"] and nodes[j] in event["url"]:
                adj_matrix[i,j] = 1
            if nodes[i] in event["domain"] and nodes[j] in event["domain"]:
                adj_matrix[i,j] = 1
            if nodes[i] in event["host"] and nodes[j] in event["host"]:
                adj_matrix[i,j] = 1
            if nodes[i] in event["region"] and nodes[j] in event["region"]:
                adj_matrix[i,j] = 1
            if nodes[i] in event["attack_technique"] and nodes[j] in event["attack_technique"]:
                adj_matrix[i,j] = 1
            if nodes[i] in event["attacker"] and nodes[j] in event["attacker"]:
                adj_matrix[i,j] = 1
            if nodes[i] in event["Vulnerability"] and nodes[j] in event["Vulnerability"]:
                adj_matrix[i,j] = 1

                print(adj_matrix[i,j])
    return adj_matrix
	
mat=com_adj_matrix(file_hash, email_address, ip_address, url_address, domain_address, host_name, region, attack_technique, attacker, cve, results)
print(len(mat[0]))
