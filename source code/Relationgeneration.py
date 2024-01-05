import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer

def generate_relation(A_iocs, B_iocs, events):
    with open('ICS_IOCs_Updated.json') as f:
        data = json.load(f)

        event_A_iocs = []

        for event in events:
            for att_id in A_iocs:
                for item in data:
                    for indicator in item['indicators']:
                        if str(att_id) == str(indicator['indicator']):
                            if 'domain' in event and str(indicator['indicator']) in event['domain']:
                                event_A_iocs.append(f"{att_id} {indicator['id']} {indicator['type']} {indicator['created']} {indicator['content']} {indicator['title']} {indicator['description']}")
                            if 'hash' in event and str(indicator['indicator']) in event['hash']:
                                event_A_iocs.append(f"{att_id} {indicator['id']} {indicator['type']} {indicator['created']} {indicator['content']} {indicator['title']} {indicator['description']}")
                            if 'ip' in event and str(indicator['indicator']) in event['ip']:
                                event_A_iocs.append(f"{att_id} {indicator['id']} {indicator['type']} {indicator['created']} {indicator['content']} {indicator['title']} {indicator['description']}")
                            if 'email' in event and str(indicator['indicator']) in event['email']:
                                event_A_iocs.append(f"{att_id} {indicator['id']} {indicator['type']} {indicator['created']} {indicator['content']} {indicator['title']} {indicator['description']}")
                            if 'url' in event and str(indicator['indicator']) in event['url']:
                                event_A_iocs.append(f"{att_id} {indicator['id']} {indicator['type']} {indicator['created']} {indicator['content']} {indicator['title']} {indicator['description']}")
                            if 'host' in event and str(indicator['indicator']) in event['host']:
                                event_A_iocs.append(f"{att_id} {indicator['id']} {indicator['type']} {indicator['created']} {indicator['content']} {indicator['title']} {indicator['description']}")
                            if 'cve' in event and str(indicator['indicator']) in event['cve']:
                                event_A_iocs.append(f"{att_id} {indicator['id']} {indicator['type']} {indicator['created']} {indicator['content']} {indicator['title']} {indicator['description']}")


            if set(event['attacker']).intersection(A_iocs):
                event_A_iocs = []
                for item in data:
                    for i in range(len(A_iocs)):
                        if A_iocs[i]==item['adversary']:
                            event_A_iocs.append(item['id']+ ' ' +item['name']+' ' +item['description']+' ' +item['author_name']+' ' +item['created']+ ' ' + str(item['adversary'])+ ' ' +str(item['targeted_countries'])+ ' ' +str(item['tags'])+ ' ' +str(item['malware_families'])+ ' ' +str(item['attack_ids'])+ ' ' +str(item['industries']))


            if set(event['attack_technique']).intersection(A_iocs):
                event_A_iocs = []
                data_index = 0
                for att_id in A_iocs:
                    found = False
                    while data_index < len(data):
                        item = data[data_index]
                        if att_id in item['attack_ids']:
                            event_A_iocs.append(att_id+ ' ' +item['name']+' ' +item['description']+' ' +item['author_name']+' ' +item['created']+ ' ' + str(item['adversary'])+ ' ' +str(item['targeted_countries'])+ ' ' +str(item['tags'])+ ' ' +str(item['malware_families'])+ ' ' +str(item['industries']))
                            found = True
                            break
                        data_index += 1
                    data_index = 0 if found else data_index

            if set(event['region']).intersection(A_iocs):
                event_A_iocs = []
                data_index = 0
                for att_id in A_iocs:
                    found = False
                    while data_index < len(data):
                        item = data[data_index]
                        if att_id in item['targeted_countries']:
                            event_A_iocs.append(f"{att_id} {item['id']} {item['name']} {item['description']} {item['author_name']} {item['created']} {item['adversary']} {item['targeted_countries']} {item['tags']} {item['malware_families']} {item['industries']}")
                            found = True
                            break
                        data_index += 1
                    data_index = 0 if found else data_index


        event_B_iocs = []

        for event in events:
            for att_id in B_iocs:
                for item in data:
                    for indicator in item['indicators']:
                        if str(att_id) == str(indicator['indicator']):
                            if 'domain' in event and str(indicator['indicator']) in event['domain']:
                                event_B_iocs.append(f"{att_id} {indicator['id']} {indicator['type']} {indicator['created']} {indicator['content']} {indicator['title']} {indicator['description']}")
                            if 'hash' in event and str(indicator['indicator']) in event['hash']:
                                event_B_iocs.append(f"{att_id} {indicator['id']} {indicator['type']} {indicator['created']} {indicator['content']} {indicator['title']} {indicator['description']}")
                            if 'ip' in event and str(indicator['indicator']) in event['ip']:
                                event_B_iocs.append(f"{att_id} {indicator['id']} {indicator['type']} {indicator['created']} {indicator['content']} {indicator['title']} {indicator['description']}")
                            if 'email' in event and str(indicator['indicator']) in event['email']:
                                event_B_iocs.append(f"{att_id} {indicator['id']} {indicator['type']} {indicator['created']} {indicator['content']} {indicator['title']} {indicator['description']}")
                            if 'url' in event and str(indicator['indicator']) in event['url']:
                                event_B_iocs.append(f"{att_id} {indicator['id']} {indicator['type']} {indicator['created']} {indicator['content']} {indicator['title']} {indicator['description']}")
                            if 'host' in event and str(indicator['indicator']) in event['host']:
                                event_B_iocs.append(f"{att_id} {indicator['id']} {indicator['type']} {indicator['created']} {indicator['content']} {indicator['title']} {indicator['description']}")
                            if 'cve' in event and str(indicator['indicator']) in event['cve']:
                                event_B_iocs.append(f"{att_id} {indicator['id']} {indicator['type']} {indicator['created']} {indicator['content']} {indicator['title']} {indicator['description']}")


            if set(event['attacker']).intersection(B_iocs):
                event_B_iocs = []
                for item in data:
                    for i in range(len(B_iocs)):
                        if B_iocs[i]==item['adversary']:
                            event_B_iocs.append(item['id']+ ' ' +item['name']+' ' +item['description']+' ' +item['author_name']+' ' +item['created']+ ' ' + str(item['adversary'])+ ' ' +str(item['targeted_countries'])+ ' ' +str(item['tags'])+ ' ' +str(item['malware_families'])+ ' ' +str(item['attack_ids'])+ ' ' +str(item['industries']))


            if set(event['attack_technique']).intersection(B_iocs):
                event_B_iocs = []
                data_index = 0
                for att_id in B_iocs:
                    found = False
                    while data_index < len(data):
                        item = data[data_index]
                        if att_id in item['attack_ids']:
                            event_B_iocs.append(att_id+ ' ' +item['name']+' ' +item['description']+' ' +item['author_name']+' ' +item['created']+ ' ' + str(item['adversary'])+ ' ' +str(item['targeted_countries'])+ ' ' +str(item['tags'])+ ' ' +str(item['malware_families'])+ ' ' +str(item['industries']))
                            found = True
                            break
                        data_index += 1
                    data_index = 0 if found else data_index

            if set(event['region']).intersection(B_iocs):
                event_B_iocs = []
                data_index = 0
                for att_id in B_iocs:
                    found = False
                    while data_index < len(data):
                        item = data[data_index]
                        if att_id in item['targeted_countries']:
                            event_B_iocs.append(f"{att_id} {item['id']} {item['name']} {item['description']} {item['author_name']} {item['created']} {item['adversary']} {item['targeted_countries']} {item['tags']} {item['malware_families']} {item['industries']}")
                            found = True
                            break
                        data_index += 1
                    data_index = 0 if found else data_index

        #print(len(B_iocs))
        #print("event",len(event_B_iocs))

        #if set(event['attacker']).intersection(B_iocs):
        #    event_B_iocs = []
        #    for item in data:
        #        for i in range(len(B_iocs)):
        #            if B_iocs[i]==item['adversary']:
        #                event_B_iocs.append(item['id']+ ' ' +item['name']+' ' +item['description']+' ' +item['author_name']+' ' +item['created']+ ' ' + str(item['adversary'])+ ' ' +str(item['targeted_countries'])+ ' ' +str(item['tags'])+ ' ' +str(item['malware_families'])+ ' ' +str(item['attack_ids'])+ ' ' +str(item['industries']))

        #print("event", event_A_iocs)
        # Generate embeddings
        model = SentenceTransformer('distilbert-base-nli-mean-tokens')
        A_embeddings = model.encode(event_A_iocs)
        B_embeddings = model.encode(event_B_iocs)
        embeddingA = np.array(A_embeddings)
        embeddingB = np.array(B_embeddings)

        print(embeddingA.shape)
        print(embeddingB.shape)

        num_features = max(embeddingA.shape[1], embeddingB.shape[1])
        embeddingA = np.pad(embeddingA, ((0, 0), (0, num_features - embeddingA.shape[1])), mode='constant')
        embeddingB = np.pad(embeddingB, ((0, 0), (0, num_features - embeddingB.shape[1])), mode='constant')
        similarity_matrix = cosine_similarity(embeddingA, embeddingB)

    return similarity_matrix

rel=[]

#Relation (Adjacency matriX): R1: attacker uses hash
R1 = generate_relation(attacker, file_hash, results)
rel.append(R1)

#Relation (Adjacency matriX): R2: attacker accesses email
R2 = generate_relation(attacker, email_address, results)
rel.append(R2)

#Relation (Adjacency matriX): R3: attacker accesses Ip adress
R3 = generate_relation(attacker, ip_address, results)
rel.append(R3)

#Relation (Adjacency matriX): R4: attacker accesses domain adress
R4 = generate_relation(attacker, domain_address, results)
rel.append(R4)

#Relation (Adjacency matriX): R5: attacker accseses url
R5 = generate_relation(attacker, url_address, results)
rel.append(R5)

#Relation (Adjacency matriX): R6: attacker accesses host adress
R6 = generate_relation(attacker, host_name, results)
rel.append(R6)

#Relation (Adjacency matriX): R7: attacker assists another attacker
R7 = generate_relation(attacker, attacker, results)
rel.append(R7)

#Relation (Adjacency matriX): R8: attacker terget region
R8 = generate_relation(attacker, region, results)
rel.append(R8)

#Relation (Adjacency matriX): R9: attacker uses technique
R9 = generate_relation(attacker, attack_technique, results)
rel.append(R9)

#Relation (Adjacency matriX): R10: ip connects to email_address
R10 = generate_relation(email_address, ip_address, results)
rel.append(R10)

#Relation (Adjacency matriX): R11: domain_name resolve to ip
R11 = generate_relation(domain_address, ip_address, results)
rel.append(R11)

#Relation (Adjacency matriX): R12: domain_adrdess registered by email_address
R12 = generate_relation(domain_address, email_address, results)
rel.append(R12)

#Relation (Adjacency matriX): R13: vulverability evolve vulnerability
#R13 = generate_relation(cve, cve, results)
#rel.append(R13)

#print(R4)

M=[]
#M1: Attacker-hash-attacker
M1 = np.dot(R1, R1.transpose())
M.append(M1)

#M2: attacker-email-email
M2 = np.dot(R2, R2.transpose())
M.append(M2)

#M3: attacker-ip-email
M3 = np.dot(R3, R3.transpose())
M.append(M3)

#M4: attacker-domain-email
M4 = np.dot(R4, R4.transpose())
M.append(M4)

#M5: attacker-url-email
M5 = np.dot(R5, R5.transpose())
M.append(M5)

#M6: attacker-host-email
M6 = np.dot(R6, R6.transpose())
M.append(M6)

#M7: attacker-attacker-attacker
M7 = np.dot(R7, R7.transpose())
#M.append(M7)

#M8: attacker-region-attacker
M8 = np.dot(R8, R8.transpose())
#M.append(M8)

#M9: attacker-technique-attacker
M9 = np.dot(R9, R9.transpose())
#M.append(M9)

#M10: email-ip-email
M10 = np.dot(R10, R10.transpose())
#M.append(M10)

#M11: domain-ip-domain
M11 = np.dot(R11, R11.transpose())
#M.append(M11)

#M12: domain-email-domain
M12 = np.dot(R12, R12.transpose())
#M.append(M12)

#M13: vul-vul-vul
#M13 = np.dot(R13, R13.transpose())
#M.append(M13)


#M16: A-E-IP-E-A
M16 = np.dot(np.dot(R2,np.dot(R10, R10.transpose())),R2.transpose())
#M.append(M16)

print("M", M)
#print(len(adjacency_matrix))
