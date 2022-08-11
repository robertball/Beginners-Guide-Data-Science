import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import matplotlib
from scipy.stats import norm
import math

font = {'size' :10}

matplotlib.rc('font', **font)

# define constants
mu = 0 # 998.8 
sigma = 1 #73.10
x1 = -3
x2 = 3

# calculate the z-transform
z1 = ( x1 - mu ) / sigma
z2 = ( x2 - mu ) / sigma

print(f"z1 = {z1} and z2 = {z2}")

x = np.arange(z1, z2, 0.001) # range of x in spec
x_all = np.arange(-5, 5, 0.001) # entire range of x, both in and out of spec
# mean = 0, stddev = 1, since Z-transform was calculated
y = norm.pdf(x,0,1)
y2 = norm.pdf(x_all,0,1)

# build the plot
fig, ax = plt.subplots(figsize=(9,4))
#plt.style.use('fivethirtyeight')
plt.plot([0, 0], [0, 0.398], 'k-')
ax.plot(x_all,y2)

# draw vertical line from (70,100) to (70, 250)

one_std_dev_x = np.arange(-1, 1, 0.001) # range of x in spec
one_std_dev_y = norm.pdf(one_std_dev_x,0,1)

one_std_dev_x_left = np.arange(-2, -1, 0.001) # range of x in spec
one_std_dev_y_left = norm.pdf(one_std_dev_x_left,0,1)

one_std_dev_x_right = np.arange(1, 2, 0.001) # range of x in spec
one_std_dev_y_right = norm.pdf(one_std_dev_x_right,0,1)

two_std_dev_x_left = np.arange(-3, -2, 0.001) # range of x in spec
two_std_dev_y_left = norm.pdf(two_std_dev_x_left,0,1)

two_std_dev_x_right = np.arange(2, 3, 0.001) # range of x in spec
two_std_dev_y_right = norm.pdf(two_std_dev_x_right,0,1)

ax.fill_between(one_std_dev_x,one_std_dev_y,0, color=(0.701960784313725, 0.698039215686275, 1)) # alpha=0.3, color='b')
ax.fill_between(one_std_dev_x_left,one_std_dev_y_left,0, color=(0.698039215686275, 0.847058823529412, 0.694117647058824))
ax.fill_between(one_std_dev_x_right,one_std_dev_y_right,0, color=(0.698039215686275, 0.847058823529412, 0.694117647058824))
ax.fill_between(two_std_dev_x_left,two_std_dev_y_left,0, color=(1, 0.698039215686275, 0.698039215686275))
ax.fill_between(two_std_dev_x_right,two_std_dev_y_right,0, color=(1, 0.698039215686275, 0.698039215686275))
ax.set_xlim([-4,4])
ax.set_ylim([0.0, 0.4]) # 1.0])
ax.set_ylabel('Probability Density')
ax.set_xlabel('Standard Deviations from Mean')
ax.xaxis.set_major_locator(ticker.MultipleLocator(1))
ax.set_xticklabels(['','','-3s','-2s','-1s','0','1s','2s','3s'])
ax.set_title('Normal / Gaussian Distribution')

height = 0.001
#height = 0.2
plt.text(-0.6, height, '34.1%', dict(size=10))
plt.text(0.3, height, '34.1%', dict(size=10))
plt.text(-1.6, height, '13.6%', dict(size=10))
plt.text(1.3, height, '13.6%', dict(size=10))
plt.text(-2.6, height, '2.1%', dict(size=10))
plt.text(2.3, height, '2.1%', dict(size=10))

plt.style.use('plot_style.txt')
#plt.show()
plt.savefig('Ball-Rague-Fig4.2.eps', bbox_inches='tight')

