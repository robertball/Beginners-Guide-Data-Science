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


def jaccard_similarity(base_case_genres: str, compartor_genres: str):
    base_case_genres = set(base_case_genres.split(';'))  # cast the list of genres to a set
    compartor_genres = set(compartor_genres.split(';'))  # cast the list of genres to a set

    numerator = len(base_case_genres.intersection(compartor_genres))
    denomenator = len(base_case_genres.union(compartor_genres))
    return float(numerator) / float(denomenator)  # cast as float to enable decimal return values


comparator = 'Adventure;Comedy'
wsj = weighted_jaccard_similarity({'total': 4, 'Adventure': 1, 'Comedy': 1, 'Sci-Fi': 1, 'Action': 1}, comparator)
js = jaccard_similarity('Adventure;Comedy;Sci-Fi;Action', comparator)

print(wsj)
print(js)
