import json
import pandas as pd
from datetime import datetime

with open('ICS_IOCs_Updated.json') as f:
    threats = json.load(f)

organizations = list(set([org for threat in threats for org in threat['industries']]))
locations = list(set([loc for threat in threats for loc in threat['targeted_countries']]))
feature_matrix = pd.DataFrame(columns= ['active_time', 'update_frequency']+ organizations + locations )

for threat in threats:
    threat_id = threat['name']
    active_time = (datetime.now() - datetime.strptime(threat['created'], "%Y-%m-%dT%H:%M:%S.%f")).days
    update_frequency = threat['revision']
    for indicator in threat['indicators']:
      if indicator['type']=='FileHash-SHA1'or indicator['type']=='FileHash-MD5' or  indicator['type'] == 'FileHash-SHA256' or  indicator['type'] == 'email' or  indicator['type'] == 'CVE' or  indicator['type'] == 'ipv4'or  indicator['type'] == 'url'or  indicator['type'] == 'domain'or  indicator['type'] == 'hostname' :
        row = {'active_time': active_time, 'update_frequency': update_frequency}
        for org in organizations:
            row[org] = 1 if org in threat['industries'] else 0
        for loc in locations:
            row[loc] = 1 if loc in threat['targeted_countries'] else 0
        feature_matrix = pd.concat([feature_matrix, pd.DataFrame([row])], ignore_index=True)

    for tech in threat['attack_ids']:
      row = {'active_time': active_time, 'update_frequency': update_frequency}
      for org in organizations:
            row[org] = 1 if org in threat['industries'] else 0
      for loc in locations:
            row[loc] = 1 if loc in threat['targeted_countries'] else 0
      feature_matrix = pd.concat([feature_matrix, pd.DataFrame([row])], ignore_index=True)

    for reg in threat['targeted_countries']:
      row = { 'active_time': active_time, 'update_frequency': update_frequency}
      for org in organizations:
            row[org] = 1 if org in threat['industries'] else 0
      for loc in locations:
            row[loc] = 1 if loc in threat['targeted_countries'] else 0
      feature_matrix = pd.concat([feature_matrix, pd.DataFrame([row])], ignore_index=True)
    if threat['adversary']=="" or threat['adversary']=="Unknown":
      continue
    else:
        row = { 'active_time': active_time, 'update_frequency': update_frequency}
        for org in organizations:
            row[org] = 1 if org in threat['industries'] else 0
        for loc in locations:
            row[loc] = 1 if loc in threat['targeted_countries'] else 0
    feature_matrix = pd.concat([feature_matrix, pd.DataFrame([row])], ignore_index=True)

feature_matrix = feature_matrix[['active_time', 'update_frequency'] + organizations + locations ]
print(feature_matrix[:18])