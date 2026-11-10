import pandas as pd

df = pd.read_json('food_services.json', encoding='utf-8')
idx = df.groupby('TypeObject')['SeatsCount'].idxmax()
best = df.loc[idx].sort_values('TypeObject')
for _, row in best.iterrows():
    print(f"{row['TypeObject']}: {row['Name']}, {row['SeatsCount']}")