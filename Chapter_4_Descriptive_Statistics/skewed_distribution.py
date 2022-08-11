from scipy.stats import skewnorm
import matplotlib.pyplot as plt
import numpy as np

fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(10,5))
#fig, ax1 = plt.subplots(1, 1)


#for a in range(-10,10, 5):
a = -10
mean, var, skew, kurt = skewnorm.stats(a, moments='mvsk')
x = np.linspace(skewnorm.ppf(0.01, a), skewnorm.ppf(0.99, a), 100)
rv = skewnorm(a)
ax1.plot(x, rv.pdf(x), 'k-', lw=2)
ax1.xaxis.set_visible(False)
ax1.yaxis.set_visible(False)
ax1.set_ylabel("Probability Density Function")
ax1.set_title("Negative/Left Skewed")

a = 0
mean, var, skew, kurt = skewnorm.stats(a, moments='mvsk')
x = np.linspace(skewnorm.ppf(0.01, a), skewnorm.ppf(0.99, a), 100)
rv = skewnorm(a)
ax2.plot(x, rv.pdf(x), 'k-', lw=2)
ax2.xaxis.set_visible(False)
ax2.set_title("Symmetrical Distribution")
ax2.yaxis.set_visible(False)

a = 10
mean, var, skew, kurt = skewnorm.stats(a, moments='mvsk')
x = np.linspace(skewnorm.ppf(0.01, a), skewnorm.ppf(0.99, a), 100)
rv = skewnorm(a)
ax3.plot(x, rv.pdf(x), 'k-', lw=2)
ax3.xaxis.set_visible(False)
ax3.set_title("Positive/Right Skewed")
ax3.yaxis.set_visible(False)

plt.suptitle("Three Normal Distributions with Different Skewness")
#plt.show()
plt.savefig('Ball-Rague-Fig4.12.eps', bbox_inches='tight')

