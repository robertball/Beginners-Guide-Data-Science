import pandas as pd
from sklearn.feature_selection import RFE
from sklearn import tree
import numpy as np

df = pd.DataFrame({
    'height': [163, 185, 167, 184, 180, 160, 175, 174],
    'weight': [54, 93, 90, 102, 88, 50, 70, 91],
    'age': [18, 22, 68, 31, 24, 25, 32, 55],
    'iq': [90, 110, 108, 88, 90, 100, 70, 130],
    'bought_lemonade': [False, False, True, False, False, False, False, True]
})

classifier = tree.DecisionTreeClassifier()
rfe = RFE(estimator=classifier, n_features_to_select=3)

features = list(df.columns[0:4])  # get the list of features (height, weight, age, and iq)
np_features = np.array(features)  # numpy array with the features names
X = df.iloc[:, 0:4]  # get the first features
y = df.iloc[:, 4].values  # the values we are trying to predict (bought lemonade)

rfe_fitted = rfe.fit(X, y)
print(f"Returns the data of the results without the names removing the eliminated feature:\n{rfe.fit_transform(X, y)}")
print(f"\nReturns the ranking of the features to keep with a '1' and a '2' for the features to eliminate:\n{rfe_fitted.ranking_}")
print(f"\nReturns the same idea as 'ranking_' but with True and False:\n{rfe_fitted.support_}")
# print(features)
print(f"\nUses the above Boolean array from 'support_' to only have the features that were not eliminated:\n{np_features[rfe_fitted.support_]} "
      f"\n*Note that you have to use Numpy arrays to use Boolean arrays to filter.")

