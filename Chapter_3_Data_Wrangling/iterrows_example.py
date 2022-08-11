import pandas as pd
import numpy as np

def create_full_name(row):
    if isinstance(row['first_name'], str) and isinstance(row['last_name'], str):  # both first_name and last_name are strings
        result = row['first_name'] + ' ' + row['last_name']
    elif isinstance(row['first_name'], str):  # only first_name is a string
        result = row['first_name']
    elif isinstance(row['last_name'], str):  # only last_name is a string
        result = row['last_name']
    else:  # neither first_name nor last_name are strings, they are both NaN
        result = np.nan 
    return result

df = pd.read_csv('royal_line.csv', index_col='ID')

df['full_name'] = df.apply(create_full_name, axis=1)

for index, row in df.iterrows():
    if isinstance(row['birth_date'], str):
        print(f"{index}: {row['full_name']} was born {row['birth_date']}.")
