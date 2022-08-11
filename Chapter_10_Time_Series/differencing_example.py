import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from statsmodels.tsa.stattools import adfuller

df = pd.read_csv('US_energy_consumption_1973_to_Jul_2021.csv', parse_dates=['Date'], index_col=['Date'])

plt.subplots(figsize=(10,5))
plt.subplot(2, 2, 1)
plt.plot(df['total'])
plt.title('Original U.S. Energy Total Consumption')

plt.subplot(2, 2, 2)
plt.title('Total Consumption Differenced')
df['total_differenced'] = df['total'].diff()  # the periods or lag has a default of 1
plt.plot(df['total_differenced'])

ax = plt.subplot(2, 2, 3)
df['cumsum'] = df['total_differenced'].cumsum()  # inverting the difference
plt.plot(df['cumsum'])
plt.title('Total Consumption Differenced Inverted')

ax = plt.subplot(2, 2, 4)
df['cumsum'] = df['total_differenced'].cumsum()
level_diff = df['total'].mean() - df['cumsum'].mean()  # difference in level
df['cumsum_plus_level'] = df['cumsum'] + level_diff  # correcting the level
plt.plot(df['cumsum_plus_level'])
plt.title('Total Consumption Differenced Inverted + Level')

plt.subplots_adjust(left=0.1,
                    bottom=0.1, 
                    right=0.9, 
                    top=0.9, 
                    wspace=0.35, 
                    hspace=0.35)


#plt.show()
plt.savefig('Ball-Rague-Fig10.9.eps', bbox_inches='tight')

print(f'ADF on total {adfuller(df["total"])[1]}')
print(f'ADF on total_differenced {adfuller(df["total_differenced"].dropna())[1]}')  # the dropna is required because the first value was made into na with the diff function
print(f'ADF on inverted {adfuller(df["cumsum"].dropna())[1]}')
print(f'ADF on inverted plus level {adfuller(df["cumsum_plus_level"].dropna())[1]}')
