import pandas as pd

df = pd.read_csv('sales.csv', sep=';', encoding='utf-8')
decreased = df[df['new_price'] < df['old_price']]
for name in decreased['name']:
    print(name)