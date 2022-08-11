import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer


def cosine_similarity_function(base_case_plot: str, comparator_plot: str):
    # this line will convert the plots from strings to vectors in a single matrix:
    tfidf_matrix = tfidf_vectorizer.fit_transform((base_case_plot, comparator_plot))
    results = cosine_similarity(tfidf_matrix[0], tfidf_matrix[1])
    return results[0][0]


def weighted_jaccard_similarity(weighted_dictionary: dict, comparator_genres: str):
    # weighted_dictionary is based on all the selections that the user has made so far
    # comparator_genres is another movie's genres that is being compared
    numerator = 0
    denominator = weighted_dictionary['total']
    for genre in comparator_genres.split(';'):
        if genre in weighted_dictionary:
            numerator += weighted_dictionary[genre]

    return numerator / denominator


def cosine_and_weighted_jaccard(genres_weighted_dictionary_dict: dict, plots: str, comparator_movie: pd.core.series.Series):
    # Perform the cosine similiarty and weighted Jaccard metrics:
    cs_result = cosine_similarity_function(plots, comparator_movie['plot'])
    wjs_result = weighted_jaccard_similarity(genres_weighted_dictionary_dict, comparator_movie['genres'])

    # Normalization:
    # The weighted Jaccard similarity result has a range from 0.0 to 1.0.
    # The cosine similarity result has a range from -1.0 to 1.0. We need to change the range for the cosine similarity result.
    # First, add 1 to the cosine similarity result so that it has a range from 0.0 to 2.0
    # Second, divide the result by 2.0 so that it has a range from 0.0 to 1.0:
    cs_result = (cs_result + 1) / 2.0

    # Weights:
    # Use a weight of 0.2 (20%) for the cosine similarity result:
    cs_result *= 0.2
    # Use a weight of 0.8 (80%) for the weighted Jaccard similarity result:
    wjs_result *= 0.8
    return wjs_result + cs_result


tfidf_vectorizer = TfidfVectorizer()

# read the list of movies into a dataframe:
df = pd.read_csv('movies.csv', index_col='IMDB_id', on_bad_lines='skip')

# setting our K to 10. In other words, we will get the K(10) closest matches
K = 10

# get the rows that has 'Back to the Future'(88763) and 'Mad Max Beyond Thunderdome'(89530) - our selections
selections = [df.loc[88763], df.loc[89530]]

# genres_weighted_dictionary is needed for the weighted Jaccard similarity index:
genres_weighted_dictionary = {'total': 0}
for el in selections:
    for genre in el['genres'].split(';'):  # the genres are separated by a semicolon
        if genre in genres_weighted_dictionary:
            genres_weighted_dictionary[genre] += 1
        else:
            genres_weighted_dictionary[genre] = 1
        genres_weighted_dictionary['total'] += 1

# combined plots are needed for the cosine similarity metric:
plots = ''
for movie in selections:
    plots += movie['plot'] + ' '

# three filters:
df = df[(df['year'] >= 1980)]  # filter out movies before 1980
df = df[(df['stars'] >= 5)]  # filter out movies less than 5 stars
df = df[(df['rating'] == 'G') | (df['rating'] == 'PG') | (df['rating'] == 'PG-13')]  # filter out movies that are not G, PG, nor PG-13

# The following evaluates each movie with the given metric.
# 'x' is the value in each row in the dataframe.
# We use 'apply' instead of map because we are dealing with multiple columns
df['multiple_metrics'] = df.apply(lambda x: cosine_and_weighted_jaccard(genres_weighted_dictionary, plots, x), axis='columns')

sorted_df = df.sort_values(by='multiple_metrics', ascending=False)

# drop the original movie selections from the results:
for movie in selections:
    sorted_df.drop(movie.name, inplace=True)
print(sorted_df['title'].head(K))
