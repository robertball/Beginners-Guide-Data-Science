import pandas as pd

df = pd.read_csv('Titanic_Passengers.csv')
contingency_table = pd.crosstab(df['Gender'], df['Lived_Died'], margins=True) # 'margins=True' shows the summary information
print(contingency_table)

