import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom

fig, (ax1, ax2) = plt.subplots(1, 2)
np.random.seed(13)
s1 = np.random.uniform(-1,1,10000)

ax1.hist(s1, 10) #, density=True)
ax1.get_xaxis().set_visible(False)
ax1.get_yaxis().set_visible(False)
ax1.set_title("Uniform Continuous")

s2 = np.random.randint(0, 5, 10000)
ax2.hist(s2) #, density=False)
ax2.set_xticks(np.arange(0, 2)) #, step=0.5))
ax2.get_xaxis().set_visible(False)
ax2.get_yaxis().set_visible(False)
ax2.set_title("Uniform Discrete")

plt.suptitle("Uniform Distributions")

#plt.show()
plt.savefig('Ball-Rague-Fig4.16.eps', bbox_inches='tight')
