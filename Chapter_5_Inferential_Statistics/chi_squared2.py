from scipy import stats
import pandas as pd
import numpy as np

df = pd.read_csv('Titanic_Passengers.csv')
contingency_table = pd.crosstab(df['Passenger_Class'], df['Lived_Died'], margins=False)

#Assigns the frequency values without getting the summaries
firstClassCount = contingency_table.iloc[0].values
secondClassCount = contingency_table.iloc[1].values
thirdClassCount = contingency_table.iloc[2].values

f_obs = np.array([firstClassCount, secondClassCount, thirdClassCount])
print(stats.chi2_contingency(f_obs)[0:3])

