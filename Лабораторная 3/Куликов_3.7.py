import pandas as pd

df = pd.read_csv('prices.csv', sep=';', encoding='utf-8').set_index('Магазин')
stacked = df.stack().reset_index()
stacked.columns = ['Магазин', 'Продукт', 'Цена']
stacked['Цена'] = stacked['Цена'].astype(int)
stacked = stacked.sort_values(['Цена', 'Продукт', 'Магазин'])
best = stacked.iloc[0]
print(f"{best['Продукт']}: {best['Магазин']}")