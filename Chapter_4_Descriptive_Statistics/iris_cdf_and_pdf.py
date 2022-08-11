import matplotlib.pyplot as plt
from scipy.stats import norm
import numpy as np

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10,5))
norm2 = norm(6.588, 0.635879593) # the mean and std. dev. of the sepal length of the Iris-virginica

x = np.linspace(norm2.ppf(0.01), norm2.ppf(0.99), 100)
ax1.plot(x, norm2.cdf(x),'b-', lw=2, alpha=0.6, label='Normal pdf (mean=0, std. dev.=2)')
ax1.set_title("CDF")
ax1.set_ylabel("Probability")
ax1.set_xlabel("Sepal Length (cm)")

x = np.linspace(norm2.ppf(0.01), norm2.ppf(0.99), 100)
ax2.plot(x, norm2.pdf(x),'r-', lw=2, alpha=0.6, label='Normal pdf (mean=0, std. dev.=1)')
ax2.set_title("PDF")
ax2.set_ylabel("Probability")
ax2.set_xlabel("Sepal Length (cm)")

fig.suptitle("The CDF and PDF of the sepal length of the Iris-Virginica")
#plt.show()
plt.savefig('Ball-Rague-Fig4.11.eps', bbox_inches='tight')

