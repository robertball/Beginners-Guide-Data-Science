import pandas as pd
from statsmodels.graphics.tsaplots import plot_acf
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('US_energy_consumption_1973_to_Jul_2021.csv', parse_dates=['Date'], index_col=['Date'])

fig, ax = plt.subplots(figsize=(10,5))
plt.subplot(2, 2, 1)
plt.plot(df.index, df.total)
plt.title('Original Data')

plt.subplot(2, 2, 2)
df['mov_avg'] = df['total'].rolling(6).mean()
plt.plot(df.index, df.mov_avg)
plt.title('6 Month Window')

plt.subplot(2, 2, 3)
df['mov_avg'] = df['total'].rolling(12).mean()
plt.plot(df.index, df.mov_avg)
plt.title('12 Month Window')

plt.subplot(2, 2, 4)
df['mov_avg'] = df['total'].rolling(48).mean()
plt.plot(df.index, df.mov_avg)
plt.title('48 Month Window')

ax.tick_params(axis='both', which='major', labelsize=3)

plt.subplots_adjust(left=0.1,
                    bottom=0.1, 
                    right=0.9, 
                    top=0.9, 
                    wspace=0.15, 
                    hspace=0.35)

#plt.show()
plt.savefig('Ball-Rague-Fig10.14.eps', bbox_inches='tight')

