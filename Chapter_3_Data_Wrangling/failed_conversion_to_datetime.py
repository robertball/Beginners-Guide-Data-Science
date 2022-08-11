import pandas as pd

df = pd.read_csv('royal_line.csv', index_col='ID')

# remove all NA rows in the birth_date column:
df['birth_date'].dropna(inplace=True)  
df['birth_date'] = pd.to_datetime(df['birth_date'])  # this fails!

