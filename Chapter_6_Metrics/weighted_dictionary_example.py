import pandas as pd


def weighted_jaccard_similarity(weighted_dictionary: dict, comparator_genres: str):
    # weighted_dictionary is based on all the selections that the user has made so far
    # comparator_genres is another movie's genres that is being compared
    numerator = 0
    denominator = weighted_dictionary['total']
    for genre in comparator_genres.split(';'):
        if genre in weighted_dictionary:
            numerator += weighted_dictionary[genre]

    return numerator / denominator


# read the list of movies into a dataframe:
df = pd.read_csv('movies.csv', index_col='IMDB_id', on_bad_lines='skip')

# put our selections of 'Back to the Future'(88763) and
# 'Mad Max Beyond Thunderome'(89530) into a list:
selections = [df.loc[88763], df.loc[89530]]

# genres_weighted_dictionary is needed for the weighted Jaccard similarity index:
genres_weighted_dictionary = {'total': 0}
for movie in selections:
    for genre in movie['genres'].split(';'):  # the genres are separated by a semicolon
        if genre in genres_weighted_dictionary:
            genres_weighted_dictionary[genre] += 1
        else:
            genres_weighted_dictionary[genre] = 1
        genres_weighted_dictionary['total'] += 1

print(f'genres_weighted_dictionary = {genres_weighted_dictionary}')
