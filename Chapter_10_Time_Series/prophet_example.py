import numpy as np
from prophet import Prophet
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('US_energy_consumption_1973_to_Jul_2021.csv', parse_dates=['Date'])

df.rename(columns={'Date': 'ds', 'total': 'y'}, inplace=True)  # prophet requires that the x-axis be 'ds' and the y-axis be 'y'
df = df[['ds', 'y']]

m = Prophet()
m.fit(df)
future = m.make_future_dataframe(periods=1460)  # predict for the next 4 years
future.tail()
forecast = m.predict(future)

fig1 = m.plot(forecast)
plt.savefig('Ball-Rague-Fig10.18.a.eps', bbox_inches='tight')
fig2 = m.plot_components(forecast)
plt.savefig('Ball-Rague-Fig10.18.b.eps', bbox_inches='tight')
#plt.show()
