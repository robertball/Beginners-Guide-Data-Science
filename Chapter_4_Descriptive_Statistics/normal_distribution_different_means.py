import matplotlib.pyplot as plt
from scipy.stats import norm
import numpy as np



fig, ax = plt.subplots(1, 1)
x = np.linspace(norm.ppf(0.001), norm.ppf(0.999), 100)
ax.plot(x, norm.pdf(x),'r-', lw=3, alpha=0.6, label='Normal pdf (mean=0, std. dev.=1)')

norm2 = norm(0, 2)
x = np.linspace(norm2.ppf(0.001), norm2.ppf(0.999), 100)
ax.plot(x, norm2.pdf(x),'b-', lw=3, alpha=0.6, label='Normal pdf (mean=0, std. dev.=2)')

norm3 = norm(2, .5)
x = np.linspace(norm3.ppf(0.001), norm3.ppf(0.999), 100)
ax.plot(x, norm3.pdf(x),'g-', lw=3, alpha=0.6, label='Normal pdf (mean=2, std. dev.=0.5)')

ax.legend(loc='best')
plt.ylim(bottom=0)

#plt.show()
plt.savefig('Ball-Rague-Fig4.9.eps', bbox_inches='tight')

