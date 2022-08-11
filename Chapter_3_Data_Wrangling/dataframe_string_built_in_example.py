import pandas as pd

df = pd.read_csv('royal_line.csv', index_col='ID')

# drops all rows with an NA in the title column:
df.dropna(inplace=True, subset=['title'])  
print(df[df.title.str.contains('Queen')])  # without brackets
print(df[df['title'].str.contains('Queen')])  # with brackets

