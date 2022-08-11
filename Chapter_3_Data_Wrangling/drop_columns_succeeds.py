import pandas as pd
df = pd.read_csv('royal_line.csv', index_col='ID')

# drop columns in a new dataframe (the old dataframe is not affected):
new_df = df.drop(columns=['birth_place', 'death_place'])  

# drop columns in the current dataframe:
df.drop(columns=['birth_place', 'death_place'], inplace=True)

