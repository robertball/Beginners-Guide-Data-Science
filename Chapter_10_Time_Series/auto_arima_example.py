import pandas as pd
from pmdarima import auto_arima
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error

df = pd.read_csv('US_energy_consumption_1973_to_Jul_2021.csv', parse_dates=['Date'], index_col=['Date'])
total = df['total']
train_size = 466  # 466 is 80% training set

# using 80/20 split:
train = total[:train_size]
test = total[train_size:]

model = auto_arima(train, start_p=1, d=1, start_q=1, seasonal=True, m=12)
print(model)
# print(model.summary())
# print(model.to_dict())

predictions = model.predict(n_periods=len(test))

plt.figure(figsize=(10,5))
plt.plot(train, label='Train')
plt.plot(test, label='Test')
plt.plot(test.index, predictions, label=f'SARIMA MSE={mean_squared_error(test, predictions):.3f}')
plt.title('SARIMA Results')
plt.legend()

#plt.show()
plt.savefig('Ball-Rague-Fig10.12.eps', bbox_inches='tight')
