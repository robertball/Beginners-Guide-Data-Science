from scipy import stats
import pandas as pd

scores = pd.Series([55, 60, 72, 78, 80, 81, 82, 83, 90, 98, 100])
print(scores.describe())
print('\n',stats.zscore(scores))

