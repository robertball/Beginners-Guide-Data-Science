import pandas as pd
df = pd.read_csv('royal_line.csv', index_col='ID')

df['full_name'] = df['first_name'] + ' ' + df['last_name']
print(df[['first_name', 'last_name', 'full_name']].head())

