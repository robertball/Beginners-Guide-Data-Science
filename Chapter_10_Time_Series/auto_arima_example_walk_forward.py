import pandas as pd
from pmdarima import arima, auto_arima
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error

df = pd.read_csv('US_energy_consumption_1973_to_Jul_2021.csv', parse_dates=['Date'], index_col=['Date'])
total = df['total']
train_size = 466  # 466 is 80% training set

# using 80/20 split:
train = total[:train_size]
test = total[train_size:]

# the best SARIMAX model found from auto_arima is ARIMA(0,1,2)(1,0,2)[12].
# this result was found by running 'auto_arima_example.py'.
model = auto_arima(train, start_p=0, d=1, start_q=2, start_P=1, D=0, start_Q=2, seasonal=True, m=12)
print(model)
# print(model.summary())
# print(model.to_dict())

# Walk forward:
predictions = []
for i in range(len(test)):
    print(i)
    predictions.append(model.predict(n_periods=1))
    model.update(total[train_size + i])

plt.figure(figsize=(10,5))
plt.plot(train, label='Train')
plt.plot(test, label='Test')
plt.plot(test.index, predictions, label=f'SARIMA MSE={mean_squared_error(test, predictions):.3f}')
plt.title('SARIMA Walk Forward Results')
plt.legend()

#plt.show()
plt.savefig('Ball-Rague-Fig10.13.eps', bbox_inches='tight')
