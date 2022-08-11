import matplotlib.pyplot as plt
import numpy as np
import math
from vectors import *

height_in_cm = [163, 185, 167, 184, 180, 160, 175, 174]
weight_in_kg = [54, 93, 90, 102, 88, 50, 70, 91]
age_in_years = [18, 22, 68, 31, 24, 25, 32, 55]
x = np.arange(len(height_in_cm))

fig = plt.figure()
ax = plt.axes(projection='3d')

for i in range(len(height_in_cm)):
    ax.scatter(height_in_cm[i], weight_in_kg[i], age_in_years[i])
ax.set_title('Height (cm), Weight (kg), and Age (years)')
ax.set_xlabel('Height (cm)')
ax.set_ylabel('Weight (kg)')
ax.set_zlabel('Age (years)')
ax.w_xaxis.set_pane_color((0.0, 0.0, 0.0, 0.0))
ax.w_yaxis.set_pane_color((0.0, 0.0, 0.0, 0.0))
ax.w_zaxis.set_pane_color((0.0, 0.0, 0.0, 0.0))

plt.style.use('plot_style.txt')
#plt.show()
plt.savefig('Ball-Rague-Fig8.22.eps', bbox_inches='tight')

