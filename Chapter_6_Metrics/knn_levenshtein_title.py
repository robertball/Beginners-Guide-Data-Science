import pandas as pd
import Levenshtein


# read the list of movies into a dataframe:
df = pd.read_csv('movies.csv', index_col='IMDB_id', on_bad_lines='skip')

# setting our K to 10. In other words, we will get the K(10) closest matches
K = 10

# get the row that has 'Back to the Future' - our base case
base_case = df.loc[88763]  # 88763 is the IMDB id for 'Back to the Future'
print(f"Comparing all movies to our base case: {base_case['title']}.")

comparison_type = "title"

# The following evaluates each movie with the given metric.
# 'x' is the value in each row in the 'comparison_type' column
df['levenshtein'] = df[comparison_type].map(lambda x: Levenshtein.distance(base_case[comparison_type], x))

sorted_df = df.sort_values(by='levenshtein')
sorted_df.drop(88763, inplace=True)
print(sorted_df['title'].head(K))
