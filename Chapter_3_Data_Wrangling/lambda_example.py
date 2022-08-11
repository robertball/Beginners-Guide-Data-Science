import pandas as pd
df = pd.read_csv('royal_line.csv', index_col='ID')

df['name_length'] = df.apply(lambda row: 0 if isinstance(row['last_name'], float) else len(row['last_name']), axis=1) 

