import pandas as pd
df = pd.read_csv('royal_line.csv', index_col='ID')

df.drop(index=1, inplace=True)  # drop a single row

df.drop(index=[4, 5, 6], inplace=True)  # drop multiple rows

