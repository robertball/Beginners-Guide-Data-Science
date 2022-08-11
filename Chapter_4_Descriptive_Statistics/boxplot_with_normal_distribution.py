import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from matplotlib.patches import ConnectionPatch
from scipy.stats import norm
import math

# define constants
mu = 0 # 998.8 
sigma = 1 #73.10
x1 = -3
x2 = 3

# calculate the z-transform
z1 = ( x1 - mu ) / sigma
z2 = ( x2 - mu ) / sigma

#print(f"z1 = {z1} and z2 = {z2}")

x = np.arange(z1, z2, 0.001) # range of x in spec
x_all = np.arange(-5, 5, 0.001) # entire range of x, both in and out of spec
# mean = 0, stddev = 1, since Z-transform was calculated
y = norm.pdf(x,0,1)
y2 = norm.pdf(x_all,0,1)


fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1, figsize=(10, 5.5))

blue_purple = (0.635294117647059, 0.623529411764706, 1)
light_blue = (0.552941176470588, 0.541176470588235, 1)
light_green = (0.643137254901961, 0.819607843137255, 0.63921568627451)
light_red = (1, 0.643137254901961, 0.650980392156863)

coordsA = "data"
coordsB = "data"
right_fifty_line = ConnectionPatch(xyA=(0.6745, 0), xyB=(1.5, 1.922), coordsA=coordsA, coordsB=coordsB, axesA=ax2, axesB=ax1, color=light_blue, arrowstyle="-")
left_fifty_line = ConnectionPatch(xyA=(-0.6745, 0), xyB=(-1.5, 1.922), coordsA=coordsA, coordsB=coordsB, axesA=ax2, axesB=ax1, color=light_blue, arrowstyle="-")
right_26_line = ConnectionPatch(xyA=(2.698, 0), xyB=(6.05, 1.96), coordsA=coordsA, coordsB=coordsB, axesA=ax2, axesB=ax1, color=light_blue, arrowstyle="-")
left_26_line = ConnectionPatch(xyA=(-2.698, 0), xyB=(-6.05, 1.96), coordsA=coordsA, coordsB=coordsB, axesA=ax2, axesB=ax1, color=light_blue, arrowstyle="-")

ax2.add_artist(right_fifty_line)
ax2.add_artist(left_fifty_line)
ax2.add_artist(right_26_line)
ax2.add_artist(left_26_line)

bplot1 = ax1.boxplot([-6.06,-2,-1.67,-1,-0.5,0.5,1,1.65,2,6.05], patch_artist=True, vert=False, positions=[2], whis=(0,100)) 
bplot1['boxes'][0].set_facecolor(blue_purple)
ax1.set_title('Boxplot with Normal Distribution')


plt.text(-.355, .565, 'Median', dict(size=12))
plt.text(-.75, .75, 'Q1', dict(size=12))
plt.text(.45, .75, 'Q3', dict(size=12))
plt.text(-0.11, .8, 'IQR', dict(size=12))
plt.text(2.0, .75, 'Q3+1.5*IQR or', dict(size=12))
plt.text(2.0, .716, 'Maximum', dict(size=12))
plt.text(-3.12, .75, 'Q1-1.5*IQR or', dict(size=12))
plt.text(-3.12, .716, 'Minimum', dict(size=12))

plt.text(-3.35, .04, '0.35%', dict(size=12))
plt.text(-1.80, .04, '24.65%', dict(size=12))
plt.text(-.19, .04, '50%', dict(size=12))
plt.text(1.09, .04, '24.65%', dict(size=12))
plt.text(2.75, .04, '0.35%', dict(size=12))


ax2.plot(x_all,y2)
fifty_percent_x = np.arange(-0.6745, 0.6745, 0.001) # range of x in spec
fifty_percent_y = norm.pdf(fifty_percent_x,0,1)

second_percent_x_right = np.arange(0.6745, 2.698, 0.001) # range of x in spec
second_percent_y_right = norm.pdf(second_percent_x_right,0,1)
second_percent_x_left = np.arange(-2.698, -0.6745, 0.001) # range of x in spec
second_percent_y_left = norm.pdf(second_percent_x_left,0,1)

third_percent_x_right = np.arange(2.698, 5, 0.001) # range of x in spec
third_percent_y_right = norm.pdf(third_percent_x_right,0,1)
third_percent_x_left = np.arange(-5, -2.698, 0.001) # range of x in spec
third_percent_y_left = norm.pdf(third_percent_x_left,0,1)

ax2.fill_between(fifty_percent_x,fifty_percent_y,0, alpha=0.3, color=blue_purple)
ax2.fill_between(second_percent_x_right,second_percent_y_right,0, alpha=0.3, color=light_green)
ax2.fill_between(second_percent_x_left,second_percent_y_left,0, alpha=0.3, color=light_green)
ax2.fill_between(third_percent_x_right,third_percent_y_right,0, alpha=0.3, color=light_red)
ax2.fill_between(third_percent_x_left, third_percent_y_left,0, alpha=0.3, color=light_red)
#plt.plot([0, 0], [0, 0.398], 'k-')  # median line


# Draw an arrow between the same point in data coordinates,
# but in different axes.
xy = (0.3, 0.2)

ax2.set_ylabel('Probability Density')
ax2.xaxis.set_major_locator(ticker.MultipleLocator(1))
ax2.set_xticklabels(['','','-3s','-2s','-1s','0','1s','2s','3s'])

ax1.axes.yaxis.set_visible(False)
ax1.axes.xaxis.set_visible(False)

ax1.set_xlim(-9.0, 9.0)
ax1.set_ylim(1.75, 2.25)
ax2.set_xlim(-4, 4)
ax2.set_ylim([0.0, 0.4])

plt.style.use('plot_style.txt')
#plt.show()
plt.savefig('Ball-Rague-Fig4.3.eps', bbox_inches='tight')

