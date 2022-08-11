import pandas as pd
df = pd.read_csv('royal_line.csv', index_col='ID')

df.drop(columns=['birth_place', 'death_place'])
print(df.head())

