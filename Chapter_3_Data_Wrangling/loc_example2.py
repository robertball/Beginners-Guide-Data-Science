import pandas as pd

df = pd.read_csv('royal_line.csv', index_col='ID')

print(df.loc[0])  # causes an error because there is no row labeled 0
print(df.iloc[0])  # works because it returns the first (zeroeth) row


