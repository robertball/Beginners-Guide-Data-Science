import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer


def cosine_similarity_function(base_case_plot, comparator_plot):
    # this line will convert the plots from strings to vectors in a single matrix:
    tfidf_matrix = tfidf_vectorizer.fit_transform((base_case_plot, comparator_plot))
    results = cosine_similarity(tfidf_matrix[0], tfidf_matrix[1])
    return results[0][0]


tfidf_vectorizer = TfidfVectorizer()

# read the list of movies into a dataframe:
df = pd.read_csv('movies.csv', index_col='IMDB_id', on_bad_lines='skip')

# setting our K to 10. In other words, we will get the K(10) closest matches
K = 10

# get the row that has 'Back to the Future' - our base case
base_case = df.loc[88763]  # 88763 is the IMDB id for 'Back to the Future'
print(f"Comparing all movies to our base case: {base_case['title']}.")

comparison_type = "plot"

# The following evaluates each movie with the given metric.
# 'x' is the value in each row in the 'comparison_type' column
df['cosine'] = df[comparison_type].map(lambda x: cosine_similarity_function(base_case[comparison_type], x))

sorted_df = df.sort_values(by='cosine', ascending=False)
sorted_df.drop(88763, inplace=True)
print(sorted_df['title'].head(K))
