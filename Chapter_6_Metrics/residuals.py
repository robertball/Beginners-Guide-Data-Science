import matplotlib.pyplot as plt
import numpy as np

X_values = np.arange(1, 8)

data = [1, 2.5, 2.9, 6, 3.8, 4.1, 8.2]
model1 = np.arange(1, 8)

plt.plot(X_values, model1, c='green')  # the model
for x, my, dy in zip(X_values, model1, data):
    plt.plot([x, x], [my, dy], c='blue')  # line from model to actual point (residuals)
plt.scatter(X_values, data, c='red')  # the actual data
plt.title(f'Depiction of Residuals (blue lines)')
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')

#plt.show()
plt.savefig('Ball-Rague-Fig6.7.eps', bbox_inches='tight')

