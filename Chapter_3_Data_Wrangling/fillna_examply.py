import pandas as pd

df = pd.read_csv('royal_line.csv', index_col='ID')

# replace ALL NA entries with a fixed value:
df.fillna(0, inplace=True)  

# replace the first 2 NA entries in each column with a fixed value:
df.fillna(0, limit=2, inplace=True)  

# replace ALL NA first names with a fixed value:
df['first_name'].fillna('no first name', inplace=True)  

# replace specific columns with specific values:
values = {'first_name': 'no_first_name', 'last_name': 'no_last_name', 'sex': 'no_sex', 'title': 'no_title', 'birth_date': 'no_birth_date', 'birth_place': 'no_birth_place', 'death_date': 'no_death_date', 'death_place': 'no_death_place'}
df.fillna(value=values, inplace=True)

# ffill and pad: from first row to last row, propagate the most recent row that # is not an NA forward until next valid row
df.fillna(method='ffill', inplace=True)  
# bfill and backfill: like ffill, except from last row to first row
df.fillna(method='bfill', inplace=True)  

