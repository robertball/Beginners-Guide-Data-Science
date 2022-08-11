import pandas as pd
from scipy import stats
import numpy as np

df = pd.read_csv('Titanic_Passengers.csv')
contingency_table = pd.crosstab(df['Gender'], df['Lived_Died'], margins=False) # 'margins=False' does NOT show the summary information

print(stats.chi2_contingency(contingency_table)[0:3])

