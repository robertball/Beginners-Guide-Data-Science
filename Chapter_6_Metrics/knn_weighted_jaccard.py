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

# setting our K to 10. In other words, we will get the K(10) closest matches
K = 10

# put our selections of 'Back to the Future'(88763) and 'Mad Max Beyond Thunderome'(89530) into a list:
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

# three filters:
df = df[(df['year'] >= 1980)]  # filter out movies before 1980
df = df[(df['stars'] >= 5)]  # filter out movies less than 5 stars
df = df[(df['rating'] == 'G') | (df['rating'] == 'PG') | (df['rating'] == 'PG-13')]  # filter out movies that are not G, PG, nor PG-13

comparison_type = "genres"

df['weighted_jaccard'] = df[comparison_type].map(lambda x: weighted_jaccard_similarity(genres_weighted_dictionary, x))

sorted_df = df.sort_values(by='weighted_jaccard', ascending=False)

# drop the original movie selections from the results:
for movie in selections:
    sorted_df.drop(movie.name, inplace=True)
print(sorted_df[['title', 'genres']].head(K))
