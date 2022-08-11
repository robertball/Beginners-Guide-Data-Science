import pandas as pd
df = pd.read_csv('royal_line.csv', index_col='ID')

df.drop(df.index[0], inplace=True)
df.drop(df.index[0], inplace=True)

