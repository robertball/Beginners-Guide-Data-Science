import pandas as pd
from statsmodels.graphics.tsaplots import plot_pacf
import matplotlib.pyplot as plt
from matplotlib.collections import PolyCollection

df = pd.read_csv('US_energy_consumption_1973_to_Jul_2021.csv', parse_dates=['Date'], index_col=['Date'])

fig, ax = plt.subplots(figsize=(10,5))
plot_pacf(df['total'], ax=ax, method='ywm')
# now we have to change the color for eps generation:
my_color = (0.780392156862745, 0.854901960784314, 0.937254901960784)
for item in ax.collections:
    if type(item)==PolyCollection:
        item.set_facecolor(my_color)

plt.title('Partial Autocorrelation for U.S. Energy Consumption')

#plt.show()
plt.savefig('Ball-Rague-Fig10.11.eps', bbox_inches='tight')
