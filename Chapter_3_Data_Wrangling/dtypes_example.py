import pandas as pd
df = pd.read_csv('royal_line.csv', index_col='ID')

print(df.info())
print(df.dtypes)

