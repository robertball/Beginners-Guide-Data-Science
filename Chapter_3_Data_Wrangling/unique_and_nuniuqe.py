import pandas as pd
df = pd.read_csv('royal_line.csv', index_col='ID')

# prints a list of the unique titles in the dataframe:
print(df['title'].unique())

print(df['title'].nunique())  # prints 308 (does NOT count NA's)
print(len(df['title'].unique()))  # prints 309 (does count NA's)

df.dropna(inplace=True, subset=['title'])  # get rid of NA's in title column
print(len(df['title'].unique()))  # now prints 308

