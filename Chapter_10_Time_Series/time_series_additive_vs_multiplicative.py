import numpy as np
import matplotlib
import matplotlib.pyplot as plt

x = np.arange(0, 30 * np.pi, 0.1)
y = np.sin(x)

trend = np.arange(len(x))

# divide y by 5 to make it more comparable visually to the additive trend
multiplicative = trend * y/5 + trend

# mulitiply y by 60 to see the ups and downs better (otherwise they are too small):
additive = trend + y*60

plt.figure(figsize=(10.5, 4))

plt.subplot(3, 2, 1)
plt.ylabel('Trend')
plt.plot(x, trend)
plt.gca().xaxis.set_major_locator(plt.NullLocator())  # remove x ticks
plt.gca().yaxis.set_major_locator(plt.NullLocator())  # remove y ticks

plt.subplot(3, 2, 2)
plt.ylabel('Trend')
plt.plot(x, trend)
plt.gca().xaxis.set_major_locator(plt.NullLocator())  # remove x ticks
plt.gca().yaxis.set_major_locator(plt.NullLocator())  # remove y ticks

plt.subplot(3, 2, 3)
plt.ylabel('Seasonal')
plt.plot(y)
plt.gca().xaxis.set_major_locator(plt.NullLocator())  # remove x ticks
plt.gca().yaxis.set_major_locator(plt.NullLocator())  # remove y ticks

plt.subplot(3, 2, 4)
plt.ylabel('Seasonal')
plt.plot(y)
plt.gca().xaxis.set_major_locator(plt.NullLocator())  # remove x ticks
plt.gca().yaxis.set_major_locator(plt.NullLocator())  # remove y ticks

plt.subplot(3, 2, 5)
plt.ylabel('Additive')
plt.plot(x, additive)
plt.gca().xaxis.set_major_locator(plt.NullLocator())  # remove x ticks
plt.gca().yaxis.set_major_locator(plt.NullLocator())  # remove y ticks

plt.subplot(3, 2, 6)
plt.ylabel('Multiplicative')
plt.plot(x, multiplicative)
plt.gca().xaxis.set_major_locator(plt.NullLocator())  # remove x ticks
plt.gca().yaxis.set_major_locator(plt.NullLocator())  # remove y ticks

plt.suptitle('Additive vs Multiplicative Seasonal Data')
plt.style.use('plot_style.txt')
#plt.show()
plt.savefig('Ball-Rague-Fig10.4.eps', bbox_inches='tight')

