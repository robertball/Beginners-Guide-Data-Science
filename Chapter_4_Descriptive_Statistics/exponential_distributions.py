from scipy.stats import expon
import matplotlib.pyplot as plt
import matplotlib
import numpy as np

font = {'size' :10}

matplotlib.rc('font', **font)


fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))

x = np.linspace(expon.ppf(0.001), expon.ppf(0.999), 100)
ax1.plot(x, expon.pdf(x), 'r-', lw=3, alpha=0.8, label='Exponential pdf (mean = 0, std. dev.=1)')
ax1.set_ylim(0, 1)
ax1.set_xlim(left=0)
ax1.legend(loc='best', fontsize=8)
ax1.set_title("Standard Exponential Distribution")
ax1.set_ylabel("Probability Density Function")


expon1 = expon(0, 1)
x = np.linspace(expon1.ppf(0.001), expon1.ppf(0.999), 100)
ax2.plot(x, expon1.pdf(x), 'r-', lw=3, alpha=0.8, label='Exponential pdf (mean = 0, std. dev.=1)')

expon2 = expon(0, 2)
x = np.linspace(expon2.ppf(0.001), expon2.ppf(0.999), 100)
ax2.plot(x, expon2.pdf(x), 'b-', lw=3, alpha=0.8, label='Exponential pdf (mean = 0, std. dev.=2)')

expon3 = expon(2, 0.5)
x = np.linspace(expon3.ppf(0.001), expon3.ppf(0.999), 100)
ax2.plot(x, expon3.pdf(x), 'g-', lw=3, alpha=0.8, label='Exponential pdf (mean = 2, std. dev.=0.5)')

ax2.set_ylim(0, 1)
ax2.set_xlim(left=0)
ax2.legend(loc='best')
ax2.set_title("Different Means and Std. Deviations")
ax2.set_ylabel("Probability Density Function")
plt.legend(fontsize=8)
plt.suptitle("Exponential Distribution Examples")

#plt.show()
plt.savefig('Ball-Rague-Fig4.13.eps', bbox_inches='tight')

