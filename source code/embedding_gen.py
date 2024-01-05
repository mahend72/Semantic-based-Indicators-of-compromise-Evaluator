from scipy.special import chdtriv
import json
from gensim.models import Word2Vec
import numpy as np


with open('ICS_IOCs_Updated.json') as f:
    ioc_dict = json.load(f)

#10 type of IOCs has been considered
file_hash = []
email_address =[]
ip_address=[]
url_address=[]
domain_address=[]
host_name=[]
region=[]
attack_technique=[]
attacker=[]
cve=[]

embedding_matrix=[]


for item in ioc_dict:
  for subitem in item['indicators']:
    if subitem['type']== 'FileHash-SHA1' or subitem['type']== 'FileHash-MD5' or subitem['type']== "FileHash-SHA256":
        file_hash.append(subitem['indicator'])
    elif subitem['type']== 'email':
        email_address.append(subitem['indicator'])
    elif subitem['type']== 'ipv4':
        ip_address.append(subitem['indicator'])
    elif subitem['type']== 'CVE':
        cve.append(subitem['indicator'])
    elif subitem['type']== 'url':
        url_address.append(subitem['indicator'])
    elif subitem['type']== 'domain':
        domain_address.append(subitem['indicator'])
    elif subitem['type']== 'hostname':
        host_name.append(subitem['indicator'])

  for subitem in range(len(item['targeted_countries'])):
    region.append(item['targeted_countries'][subitem])

  for subitem in range(len(item['attack_ids'])):
    attack_technique.append(item['attack_ids'][subitem])

  if item['adversary']=="" or item['adversary']=="Unknown":
    continue
  else:
    attacker.append(item['adversary'])


# tokenize IOCs
hash_tokens = [hs.split(' ') for hs in file_hash]
email_tokens = [email.split('@') for email in email_address]
ip_tokens = [ip.split('.') for ip in ip_address]
url_tokens = [dns.split('.') for dns in url_address]
domain_tokens = [dm.split('.') for dm in domain_address]
host_tokens = [dns.split('@') for dns in host_name]
region_tokens = [reg.split(' ') for reg in region]
attack_technique_tokens = [at.split('.') for at in attack_technique]
attacker_tokens = [atr.split('.') for atr in attacker]
cve_tokens = [cv.split('-') for cv in cve]

# train Word2Vec model

all_tokens = hash_tokens + email_tokens + ip_tokens + url_tokens + domain_tokens + host_tokens +region_tokens + attack_technique_tokens + attacker_tokens
model = Word2Vec(all_tokens, vector_size=len(all_tokens), window=5, min_count=1, workers=4)

print(hash_tokens[0])


# generate embeddings
hash_embeddings = [model.wv[hs] for hs in hash_tokens]
embedding_matrix.append(hash_embeddings)
email_embeddings = [model.wv[em] for em in email_tokens]
embedding_matrix.append(email_embeddings)
ip_embeddings = [model.wv[ip] for ip in ip_tokens]
embedding_matrix.append(ip_embeddings)
url_embeddings = [model.wv[dns] for dns in url_tokens]
embedding_matrix.append(url_embeddings)
domain_embeddings = [model.wv[ip] for ip in domain_tokens]
embedding_matrix.append(domain_embeddings)
host_embeddings = [model.wv[ht] for ht in host_tokens]
embedding_matrix.append(host_embeddings)
cve_embeddings = [model.wv[chdtriv] for cv in cve_tokens]
embedding_matrix.append(cve_embeddings)
region_embeddings = [model.wv[reg] for reg in region_tokens]
embedding_matrix.append(region_embeddings)
attack_technique_embeddings = [model.wv[at] for at in attack_technique_tokens]
embedding_matrix.append(attack_technique_embeddings)
attacker_embeddings = [model.wv[atr] for atr in attacker_tokens]
embedding_matrix.append(attacker_embeddings)

all_embeddings1 = [model.wv[al] for al in all_tokens]

all_embeddings = []
for tokens in all_tokens:
    token_str = ' '.join(tokens)
    if token_str in model.wv:
        embedding = model.wv[token_str]
    else:
        # Use a placeholder vector for out-of-vocabulary tokens
        embedding = np.zeros(model.vector_size)
    all_embeddings.append(embedding.flatten())

all_embeddings = np.stack(all_embeddings)

#print(len(all_embeddings1))
print(len(all_embeddings))