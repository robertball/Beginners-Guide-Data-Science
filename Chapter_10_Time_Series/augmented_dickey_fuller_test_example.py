from statsmodels.tsa.stattools import adfuller
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('US_energy_consumption_1973_to_Jul_2021.csv', parse_dates=['Date'], index_col=['Date'])

for column in df.columns:
    p_value = adfuller(df[column])[1]
    print(f'{column}: {p_value:.2f}')

fig, ax = plt.subplots(figsize=(10,7))
df['coal'].plot(ax=ax)
df['nuclear'].plot(ax=ax)
df['crude_oil'].plot(ax=ax)
#df['natural_gas'].plot(ax=ax)
#df.plot(ax=ax)
plt.title('US Energy Consumption by type')
plt.legend()  #loc='center')

#plt.show()
#plt.savefig('Ball-Rague-Fig10.8.eps', bbox_inches='tight')
plt.savefig('Ball-Rague-Fig10.8.png', bbox_inches='tight')

