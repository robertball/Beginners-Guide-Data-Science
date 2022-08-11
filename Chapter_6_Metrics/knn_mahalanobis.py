import pandas as pd
import numpy as np
from sklearn.preprocessing import MultiLabelBinarizer
from scipy.stats import chi2


# create function to calculate Mahalanobis distance
def mahalanobis(data_input: pd.core.frame.DataFrame):
    data_mu = data_input - np.mean(data_input)
    cov = np.cov(data_input.values.T)
    inverse_cov_matrix = np.linalg.inv(cov)
    left = np.dot(data_mu, inverse_cov_matrix)
    mahal = np.dot(left, data_mu.T)
    return mahal.diagonal()


# read the list of movies into a dataframe:
df = pd.read_csv('movies.csv', index_col='IMDB_id', on_bad_lines='skip')

# setting our K to 10. In other words, we will get the K(10) closest matches
K = 10

# get the row that has 'Back to the Future' - our base case
base_case = df.loc[88763]  # 88763 is the IMDB id for 'Back to the Future'
print(f"Comparing all movies to our base case: {base_case['title']}.")

# convert the string of genres to a list:
df['genres_list'] = [x.split(';') for x in df['genres']]

# convert the list of genres to individual columns
mlb = MultiLabelBinarizer()
finalDf = pd.DataFrame(mlb.fit_transform(df['genres_list']), columns=mlb.classes_, index=df.index)

# combine the year and the different genre columns together
finalDf = pd.concat([df['year'], finalDf], axis=1)

# calculate the Mahalanobis distance for each movie:
finalDf['mahalanobis'] = mahalanobis(finalDf)

# add the columns title and genres for the final result
finalDf = pd.concat([df[['title', 'genres']], finalDf], axis=1)

# sort the results based on the Mahalanobis distance:
sorted_df = finalDf.sort_values(by='mahalanobis')

# find the actual location of Back to the Future:
# 88763 is the current index, but not its location in the sorted dataframe.
base_case_location = sorted_df.index.get_loc(88763)

# reset the index to easily get the 5 above and 5 below movies that are closest to Back to the Future:
sorted_df.reset_index(inplace=True)
k_div_2 = K // 2  # since K = 10, k_div_2 = 5
sorted_df.drop(base_case_location, inplace=True)  # drop Back to the Future from the results
# print the k_div_2 (5) movies below and above where Back to the Future was in the dataframe:
print(sorted_df[['title', 'mahalanobis']].loc[base_case_location - k_div_2:base_case_location + k_div_2])
