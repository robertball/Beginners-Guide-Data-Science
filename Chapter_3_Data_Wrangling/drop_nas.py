import pandas as pd
df = pd.read_csv('royal_line.csv', index_col='ID')

print(df.shape)  # prints (3009, 8)
df.dropna(inplace=True)
print(df.shape)  # prints (77, 8)

