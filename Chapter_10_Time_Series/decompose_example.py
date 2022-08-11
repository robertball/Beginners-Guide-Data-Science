import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose

plt.rcParams['figure.figsize'] = [10, 5.5]
plt.rc('font', size=8)

df = pd.read_csv('US_energy_consumption_1973_to_Jul_2021.csv', parse_dates=['Date'], index_col=['Date'])

#plt.figure(figsize=(10.5, 4))
result = seasonal_decompose(df['total'], model='additive')
result.plot()
plt.suptitle('Decomposition of Total U.S. Energy Consumption')

plt.subplots_adjust(left=0.1,
                    bottom=0.1, 
                    right=0.9, 
                    top=0.9, 
                    wspace=0.35, 
                    hspace=0.35)

plt.style.use('plot_style.txt')
#plt.show()
plt.savefig('Ball-Rague-Fig10.6.eps', bbox_inches='tight')

