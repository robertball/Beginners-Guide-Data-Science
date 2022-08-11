import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np

# df = yf.download('AAPL', start='2016-11-18')  # use this if you want to get the data from Yahoo
# df.to_csv('aapl_stock.csv')
df = pd.read_csv('aapl_stock.csv')  # use this if you want to use the csv file

df['Date'] = pd.to_datetime(df['Date'])

lin_reg_clf = LinearRegression()
X = np.arange(len(df['Close'])).reshape(-1, 1)
lin_reg_clf.fit(X, df['Close'])
linear_regression_line = lin_reg_clf.predict(X)

plt.plot(df['Date'], df['Close'], label='AAPL stock price')
plt.plot(df['Date'], linear_regression_line, linestyle='dotted', label='Trend line (linear regression)')
plt.title('Apple Stock (AAPL) Price over Time')
plt.ylabel('Price')
plt.xlabel('Year')
plt.legend()

#plt.show()
plt.savefig('Ball-Rague-Fig10.2.eps', bbox_inches='tight')

