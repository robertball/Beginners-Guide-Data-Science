import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

df = pd.read_csv('US_energy_consumption_1973_to_Jul_2021.csv', parse_dates=['Date'])

fig, ax = plt.subplots(figsize=(10.5, 4))
ax.plot(df.Date, df.total)
ax.xaxis.set_major_locator(matplotlib.dates.YearLocator(5))  # only show every fifth year
ax.xaxis.set_major_formatter(matplotlib.dates.DateFormatter('%Y'))
ax.set_title('Monthly U.S. Energy Consumption from January 1973 to July 2021')
ax.set_ylabel('British Thermal Units (BTU) in Quadrillions')
ax.set_xlabel('Date')
plt.style.use('plot_style.txt')
#plt.show()
plt.savefig('Ball-Rague-Fig10.1.eps', bbox_inches='tight')

