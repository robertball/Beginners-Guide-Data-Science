from scipy import stats
import pandas as pd
import numpy as np

df = pd.read_csv('Titanic_Passengers.csv')
contingency_table = pd.crosstab(df['Passenger_Class'], df['Lived_Died'], margins=False)
firstClassCount = contingency_table.iloc[0].values
secondClassCount = contingency_table.iloc[1].values
thirdClassCount = contingency_table.iloc[2].values

print('Fisher\'s 1 and 2:')
oddsratio, pvalue = stats.fisher_exact(np.array([firstClassCount, secondClassCount]))
print(pvalue)

print('Fisher\'s 1 and 3:')
oddsratio, pvalue = stats.fisher_exact(np.array([firstClassCount, thirdClassCount]))
print(pvalue)

print('Fisher\'s 2 and 3:')
oddsratio, pvalue = stats.fisher_exact(np.array([secondClassCount, thirdClassCount]))
print(pvalue)

