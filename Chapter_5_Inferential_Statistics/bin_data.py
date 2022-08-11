import pandas as pd
from scipy import stats

df = pd.read_csv('Titanic_Passengers.csv')
df['age_bins'] = pd.cut(x=df['Age'], bins=[0,10,20,30,40,50,60,70,80])

contingency_table = pd.crosstab(df['age_bins'], df['Lived_Died'], margins=True)
print(contingency_table)

print('\n', stats.chi2_contingency(pd.crosstab(df['age_bins'], df['Lived_Died']))[0:3])

