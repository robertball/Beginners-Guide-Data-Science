import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import mean_squared_error

weight = [204.4, 204.8, 203.4, 203.2, 203.2, 203.0, 202.8, 202.0, 202.2, 200.2, 202.2, 202.4, 202.2, 200.6, 200.4, 200.6, 200.8, 200.8, 199.2, 199.6, 200.0, 198.8, 199.2, 200.8, 198.4, 201.0, 199.4, 200, 199.8, 199, 199.8, 198.6, 199.4, 197.6, 198.6, 198.2, 198.8, 196.8, 198.8, 198.6, 197.6, 198.4, 198.4, 197.8, 196.6, 197, 196.2, 199.2, 197.8, 197.2, 196.4, 196.6, 197.6, 196, 198.6, 196.2, 198, 195.8, 195.8, 197.2, 196.2, 195.6]

index = [x for x in range(len(weight))]

fig, axs = plt.subplots()
axs.plot(index, weight, 'ro-')
axs.set(xlabel='Day on diet', ylabel='Weight (lbs.)')
fig.suptitle('Body Weight Fluctuations During a Diet')

#plt.show()
plt.savefig('Ball-Rague-Fig6.5.eps', bbox_inches='tight')

