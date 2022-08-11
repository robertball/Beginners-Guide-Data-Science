import pandas as pd


def jaccard_similarity(base_case_genres: str, compartor_genres: str):
    base_case_genres = set(base_case_genres.split(';'))  # cast the list of genres to a set
    compartor_genres = set(compartor_genres.split(';'))  # cast the list of genres to a set

    numerator = len(base_case_genres.intersection(compartor_genres))
    denomenator = len(base_case_genres.union(compartor_genres))
    return float(numerator) / float(denomenator)  # cast as float to enable decimal return values


# read the list of movies into a dataframe:
df = pd.read_csv('movies.csv', index_col='IMDB_id', on_bad_lines='skip')

# setting our K to 10. In other words, we will get the K(10) closest matches
K = 10

# get the row that has 'Back to the Future' - our base case
base_case = df.loc[88763]  # 88763 is the IMDB id for 'Back to the Future'
print(f"Comparing all movies to our base case: {base_case['title']}.")

comparison_type = "genres"

df = df[(df['year'] >= 1980)]  # filter out movies before 1980

# The following evaluates each movie with the given metric.
# 'x' is the value in each row in the 'comparison_type' column
df['jaccard'] = df[comparison_type].map(lambda x: jaccard_similarity(base_case[comparison_type], x))

sorted_df = df.sort_values(by='jaccard', ascending=False)
sorted_df.drop(88763, inplace=True)
print(sorted_df['title'].head(K))
