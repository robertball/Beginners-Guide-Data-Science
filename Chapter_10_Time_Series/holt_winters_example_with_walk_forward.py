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
pred = model.predict(start=test.index[0], end=test.index[-1])  # this predicts for several years

# we will walk-forward with a prediction of the next month then update the model and repeat until done:
walk_forward_predictions = []
for i in range(len(test)):
    walk_forward_predictions.append(model.predict(start=test.index[i], end=test.index[i]))
    train[test.index[i]] = test[i]  # append the value from the test series to the train series
    model = ExponentialSmoothing(train, seasonal='add').fit()  # update the model with the new value

plt.figure(figsize=(10,5))
plt.plot(train.index, train, label='Train')
plt.plot(test.index, test, label='Test')
plt.plot(pred.index, pred, label=f'Holt-Winters 80/20 split MSE={mean_squared_error(test, pred):.3f}')
plt.plot(pred.index, walk_forward_predictions, label=f'Holt-Winters w/ Walk Forward MSE={mean_squared_error(test, walk_forward_predictions):.3f}')
plt.legend(loc='best')
plt.suptitle('Holt-Winters Forecasting with U.S. Total Energy Consumption')
plt.xlabel('Year')

#plt.show()
plt.savefig('Ball-Rague-Fig10.16.eps', bbox_inches='tight')

