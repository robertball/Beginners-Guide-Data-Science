import pandas as pd
df = pd.read_csv('royal_line.csv', index_col='ID')

df.drop(df.index[:10], inplace=True)  # drop the first ten rows

df.drop(index=[11, 12, 13], columns=['birth_place'], inplace=True)  # drop rows and columns
