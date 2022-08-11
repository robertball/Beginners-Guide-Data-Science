import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 20 * np.pi, 0.1)
length = len(x)
constant_line = [5] * length
x_axis = np.arange(length)
sine_wave = np.sin(x)

fig, ax = plt.subplots(figsize=(10.5, 4))

plt.subplot(4, 3, 1)
plt.plot(x_axis, constant_line)
plt.title('No seasonality')
plt.gca().xaxis.set_major_locator(plt.NullLocator())  # remove x ticks
plt.gca().yaxis.set_major_locator(plt.NullLocator())  # remove y ticks
plt.ylabel('Constant level', rotation=0, fontsize=12, labelpad=45)

plt.subplot(4, 3, 2)
additive = constant_line + sine_wave*60
plt.plot(x_axis, additive)
plt.gca().set_ylim(-250, 250)
plt.title('Additive seasonality')
plt.gca().xaxis.set_major_locator(plt.NullLocator())  # remove x ticks
plt.gca().yaxis.set_major_locator(plt.NullLocator())  # remove y ticks

plt.subplot(4, 3, 3)
# the following line should be: constant_line * sine_wave + constant_line
# However, it doesn't matter, since multiplicative and additive are the same for a constant trend
# and since it is visually we want it to look exactly the same
# and getting the ylim exactly the same is taking too long.
multiplicative = constant_line + sine_wave*60
plt.plot(x_axis, multiplicative)
plt.gca().set_ylim(-250, 250)
plt.title('Multiplicative seasonality')
plt.gca().xaxis.set_major_locator(plt.NullLocator())  # remove x ticks
plt.gca().yaxis.set_major_locator(plt.NullLocator())  # remove y ticks

plt.subplot(4, 3, 4)
linear_trend = np.arange(0, length)
plt.plot(x_axis, linear_trend)
plt.gca().xaxis.set_major_locator(plt.NullLocator())  # remove x ticks
plt.gca().yaxis.set_major_locator(plt.NullLocator())  # remove y ticks
plt.ylabel('Linear trend', rotation=0, fontsize=12, labelpad=39)

plt.subplot(4, 3, 5)
additive = linear_trend + sine_wave*60
plt.plot(x_axis, additive)
plt.gca().xaxis.set_major_locator(plt.NullLocator())  # remove x ticks
plt.gca().yaxis.set_major_locator(plt.NullLocator())  # remove y ticks

plt.subplot(4, 3, 6)
multiplicative = linear_trend * sine_wave/5 + linear_trend
plt.plot(x_axis, multiplicative)
plt.gca().xaxis.set_major_locator(plt.NullLocator())  # remove x ticks
plt.gca().yaxis.set_major_locator(plt.NullLocator())  # remove y ticks

plt.subplot(4, 3, 7)
damped_trend = []
exp_variable = 314.5
i = 0.0
for x in range(length):
    damped_trend.append(i)
    i += 1 + exp_variable
    exp_variable -= 0.5

plt.plot(x_axis, damped_trend)
plt.gca().xaxis.set_major_locator(plt.NullLocator())  # remove x ticks
plt.gca().yaxis.set_major_locator(plt.NullLocator())  # remove y ticks
plt.ylabel('Damped trend', rotation=0, fontsize=12, labelpad=45)

plt.subplot(4, 3, 8)
additive = damped_trend + sine_wave*6000
plt.plot(x_axis, additive)
plt.gca().xaxis.set_major_locator(plt.NullLocator())  # remove x ticks
plt.gca().yaxis.set_major_locator(plt.NullLocator())  # remove y ticks

plt.subplot(4, 3, 9)
multiplicative = damped_trend * sine_wave/5 + damped_trend
plt.plot(x_axis, multiplicative)
plt.gca().xaxis.set_major_locator(plt.NullLocator())  # remove x ticks
plt.gca().yaxis.set_major_locator(plt.NullLocator())  # remove y ticks

plt.subplot(4, 3, 10)
exponential_trend = []
exp_variable = 0.0
i = 0.0
for x in range(length):
    exponential_trend.append(i)
    i += 1 + exp_variable
    exp_variable += 0.5

plt.plot(x_axis, exponential_trend)
plt.gca().xaxis.set_major_locator(plt.NullLocator())  # remove x ticks
plt.gca().yaxis.set_major_locator(plt.NullLocator())  # remove y ticks
plt.ylabel('Exponential trend', rotation=0, fontsize=12, labelpad=55)

plt.subplot(4, 3, 11)
additive = exponential_trend + sine_wave*6000
plt.plot(x_axis, additive)
plt.gca().xaxis.set_major_locator(plt.NullLocator())  # remove x ticks
plt.gca().yaxis.set_major_locator(plt.NullLocator())  # remove y ticks

plt.subplot(4, 3, 12)
multiplicative = exponential_trend * sine_wave/5 + exponential_trend
plt.plot(x_axis, multiplicative)
plt.gca().xaxis.set_major_locator(plt.NullLocator())  # remove x ticks
plt.gca().yaxis.set_major_locator(plt.NullLocator())  # remove y ticks

plt.suptitle('Types of Trends with Seasonality')
plt.tight_layout()
plt.subplots_adjust(wspace=0, hspace=0)

plt.style.use('plot_style.txt')
#plt.show()
plt.savefig('Ball-Rague-Fig10.5.eps', bbox_inches='tight')

