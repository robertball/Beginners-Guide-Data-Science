import matplotlib.pyplot as plt
import numpy as np
import math
from vectors import *

height_in_cm = [163, 185, 167, 184, 180, 160, 175, 174]
weight_in_kg = [54, 93, 90, 102, 88, 50, 70, 91]
age_in_years = [18, 22, 68, 31, 24, 25, 32, 55]
x = np.arange(len(height_in_cm))

#plt.scatter(x, height_in_cm)  # all dots are a single color
for i in range(len(height_in_cm)):  # this for loop gives each dot a different color.
    plt.scatter(height_in_cm[i], weight_in_kg[i])

plt.ylabel("Weight (kg)")
plt.xlabel("Height (cm)")
plt.title("Sample of 8 people's height & weight")

#plt.show()
plt.savefig('Ball-Rague-Fig8.21.eps', bbox_inches='tight')
