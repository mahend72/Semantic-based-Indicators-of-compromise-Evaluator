import json

with open('ICS_IOCs_Updated.json') as f:
    ioc_dict = json.load(f)

results = []

for item in ioc_dict:
  hash1 = []
  email1 =[]
  ip1= []
  url1= []
  domain1 =[]
  host1 =[]
  region1=[]
  attack_technique1=[]
  attacker1=[]
  cve1=[]

  res ={}
  for subitem in item['indicators']:
    if subitem['type'] == 'FileHash-SHA1' or subitem['type']== 'FileHash-MD5' or subitem['type'] == 'FileHash-SHA256':
        hash1.append(subitem['indicator'])
    elif subitem['type']== 'email':
        email1.append(subitem['indicator'])
    elif subitem['type']== 'CVE':
        cve1.append(subitem['indicator'])
    elif subitem['type']== 'ipv4':
        ip1.append(subitem['indicator'])
    elif subitem['type']== 'url':
        url1.append(subitem['indicator'])
    elif subitem['type']== 'domain':
        domain1.append(subitem['indicator'])
    elif subitem['type']== 'hostname':
        host1.append(subitem['indicator'])

  for subitem in range(len(item['targeted_countries'])):
    region1.append(item['targeted_countries'][subitem])

  for subitem in range(len(item['attack_ids'])):
    attack_technique1.append(item['attack_ids'][subitem])

  attacker1.append(item['adversary'])

  res['hash']=hash1
  res['email']=email1
  res['ip']=ip1
  res['url']=url1
  res['domain']=domain1
  res['host']=host1
  res['region']=region1
  res['attack_technique']=attack_technique1
  res['attacker']=attacker1
  res['Vulnerability']=cve1
  results.append(res)

with open('events.json', 'w') as ev:
    json.dump(results, ev, indent=4)