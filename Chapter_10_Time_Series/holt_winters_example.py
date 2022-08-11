import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.holtwinters import ExponentialSmoothing
from sklearn.metrics import mean_squared_error

df = pd.read_csv('US_energy_consumption_1973_to_Jul_2021.csv', parse_dates=['Date'], index_col=['Date'])

total = df['total']
total.index.freq = 'M'

train = total.iloc[:466]
test = df['total'].iloc[466:]  # 466 is 80% training set
model = ExponentialSmoothing(train, seasonal='add').fit()
pred = model.predict(start=test.index[0], end=test.index[-1])

plt.figure(figsize=(10,5))
plt.plot(train.index, train, label='Train')
plt.plot(test.index, test, label='Test')
plt.plot(pred.index, pred, label=f'Holt-Winters MSE={mean_squared_error(test, pred):.3f}')
plt.legend(loc='best')
plt.suptitle('Holt-Winters Forecasting with U.S. Total Energy Consumption')
plt.xlabel('Year')

#plt.show()
plt.savefig('Ball-Rague-Fig10.15.eps', bbox_inches='tight')

