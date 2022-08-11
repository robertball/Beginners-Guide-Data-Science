import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

df = pd.read_csv('US_energy_consumption_1973_to_Jul_2021.csv', parse_dates=['Date'])

df = df[(df['Date'] > '2016-12-01') & (df['Date'] < '2020-01-01')]

fig, ax = plt.subplots(figsize=(10.5, 4))
ax.plot(df.Date, df.total)
ax.set_title('Monthly U.S. Energy Consumption from January 2017 to January 2020')
ax.set_ylabel('British Thermal Units (BTU) in Quadrillions')
ax.set_xlabel('Date')
plt.style.use('plot_style.txt')
#plt.show()
plt.savefig('Ball-Rague-Fig10.3.eps', bbox_inches='tight')

