import pandas as pd
df = pd.read_csv('royal_line.csv', index_col='ID')

df['birth_year'] = 42

