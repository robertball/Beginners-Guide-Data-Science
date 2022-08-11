import pandas as pd

df = pd.read_csv('royal_line.csv', index_col='ID')

print(df.groupby('title')['sex'].value_counts().loc[lambda x: x >= 50])

