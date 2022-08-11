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

plt.plot(df['Date'], df['Close'], label='AAPL stock price')

# first section: from 2016-11-18 to 2019-01-01
first_section = df[(df['Date'] >= '2016-11-18') & (df['Date'] <= '2019-01-01')]
X = np.arange(len(first_section['Close'])).reshape(-1, 1)
lin_reg_clf.fit(X, first_section['Close'])
linear_regression_line = lin_reg_clf.predict(X)
plt.plot(first_section['Date'], linear_regression_line, label='Trend line (Component 1)')

# second section: from 2019-01-02 to 2020-08-01
second_section = df[(df['Date'] >= '2019-01-02') & (df['Date'] <= '2020-08-01')]
X = np.arange(len(second_section['Close'])).reshape(-1, 1)
lin_reg_clf.fit(X, second_section['Close'])
linear_regression_line = lin_reg_clf.predict(X)
plt.plot(second_section['Date'], linear_regression_line, label='Trend line (Component 2)')

# third section: from 2020-08-02 to end
second_section = df[(df['Date'] >= '2020-08-02')]
X = np.arange(len(second_section['Close'])).reshape(-1, 1)
lin_reg_clf.fit(X, second_section['Close'])
linear_regression_line = lin_reg_clf.predict(X)
plt.plot(second_section['Date'], linear_regression_line, label='Trend line (Component 3)')

plt.title('Apple Stock (AAPL) Price over Time')
plt.ylabel('Price')
plt.xlabel('Year')
plt.legend()

plt.style.use('plot_style.txt')
#plt.show()
plt.savefig('Ball-Rague-Fig10.7.eps', bbox_inches='tight')

