import pandas as pd
from statsmodels.graphics.tsaplots import plot_acf
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.collections import PolyCollection

df = pd.read_csv('US_energy_consumption_1973_to_Jul_2021.csv', parse_dates=['Date'], index_col=['Date'])

x = np.arange(0, 10 * np.pi, 0.1)
y = np.sin(x)

plt.subplots(figsize=(10,5))
plt.subplot(2, 2, 1)
plt.title("Traditional Sine Wave")
plt.plot(x, y)

ax = plt.subplot(2, 2, 2)
plot_acf(y, ax=ax)

# now we have to change the color for eps generation:
my_color = (0.776470588235294, 0.858823529411765, 0.925490196078431)
for item in ax.collections:
    if type(item)==PolyCollection:
        item.set_facecolor(my_color)

plt.subplot(2, 2, 3)
plt.title('U.S. Total Energy Consumption')
plt.plot(df['total'])

ax = plt.subplot(2, 2, 4)
plot_acf(df['total'], ax=ax)

# now we have to change the color for eps generation:
my_color = (0.776470588235294, 0.858823529411765, 0.925490196078431)
for item in ax.collections:
    if type(item)==PolyCollection:
        item.set_facecolor(my_color)

plt.subplots_adjust(left=0.1,
                    bottom=0.1, 
                    right=0.9, 
                    top=0.9, 
                    wspace=0.35, 
                    hspace=0.35)

#plt.show()
plt.savefig('Ball-Rague-Fig10.10.eps', bbox_inches='tight')

sine_series = pd.Series(y)
print(f'Pearson correlation between the time series and itself with lag of 1 observation:')
print(f'Sine wave correlation: {sine_series.autocorr(lag=1)}.')
print(f'Total energy consumption correlation: {df["total"].autocorr(lag=1)}.')
