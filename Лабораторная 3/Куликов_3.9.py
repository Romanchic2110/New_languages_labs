import pandas as pd
import json

df = pd.read_csv('playgrounds.csv', sep=';', encoding='utf-8')
result = {}
for (adm, district), group in df.groupby(['AdmArea', 'District']):
    result.setdefault(adm, {})[district] = group['Address'].tolist()

with open('addresses.json', 'w', encoding='utf-8') as f:
    json.dump(result, f, ensure_ascii=False, indent=3)