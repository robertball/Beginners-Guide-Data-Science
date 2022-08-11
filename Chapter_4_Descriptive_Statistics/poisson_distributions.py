from scipy.stats import poisson
import matplotlib.pyplot as plt
import matplotlib
import numpy as np

font = {'size' :10}

matplotlib.rc('font', **font)

fig, (ax2) = plt.subplots(1, 1, figsize=(10, 5))

poisson1x = np.arange(0, 20, 1)
poisson1 = poisson.pmf(poisson1x, mu=1)
ax2.plot(poisson1x, poisson1, 'r-', lw=3, alpha=0.8, label='Poisson pmf (lambda = 1)')

poisson2x = np.arange(0, 20, 1)
poisson2 = poisson.pmf(poisson2x, mu=4)
ax2.plot(poisson2x, poisson2, 'b-', lw=3, alpha=0.8, label='Poisson pmf (lambda = 4)')

poisson3x = np.arange(0, 20, 1)
poisson3 = poisson.pmf(poisson3x, mu=10)
ax2.plot(poisson3x, poisson3, 'g-', lw=3, alpha=0.8, label='Poisson pmf (lambda = 10)')

ax2.set_ylim(0, 0.4)
ax2.set_xlim(left=0, right=20)
ax2.legend(loc='best')
ax2.set_title("Poisson Distribution Examples")
ax2.set_ylabel("Probability Mass Function")

#plt.show()
plt.savefig('Ball-Rague-Fig4.15.eps', bbox_inches='tight')
