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

# calculate p-value for each mahalanobis distance
finalDf['p'] = 1 - chi2.cdf(finalDf['mahalanobis'], len(finalDf.columns) - 1)

# only get the biggest outliers:
sensitivity = 0.000000001
finalDf['ss'] = finalDf['p'] < sensitivity
only_ss = finalDf[finalDf['ss'] == True]

print(only_ss[['title', 'year', 'genres']])
