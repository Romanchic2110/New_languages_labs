import pandas as pd

df = pd.read_csv('data.csv', encoding='utf-8')
df['domain'] = df['email'].str.split('@').str[1]
usage = df['domain'].value_counts().reset_index()
usage.columns = ['domain', 'count']
usage = usage.sort_values(['count', 'domain']).reset_index(drop=True)
usage.to_csv('domain_usage.csv', index=False, encoding='utf-8')