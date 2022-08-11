import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error
import numpy as np

X_values = np.arange(1, 8)

data = [1, 2.5, 2.9, 6, 3.8, 4.1, 8.2]

model1 = np.arange(1, 8)
model2 = np.arange(0, 7, 1.1)
model3 = np.arange(1.5, 9, 1.15)

plt.plot(X_values, model1, c='green', label=f'MSE = {mean_squared_error(data, model1):.2f}')  # the model
plt.plot(X_values, model2, c='blue', label=f'MSE = {mean_squared_error(data, model2):.2f}')  # the model
plt.plot(X_values, model3, c='orange', label=f'MSE = {mean_squared_error(data, model3):.2f}')  # the model
plt.scatter(X_values, data, c='red')  # the actual data
plt.title(f'Mean Square Error (MSE) Example')
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
plt.legend()

#plt.show()
plt.savefig('Ball-Rague-Fig6.8.eps', bbox_inches='tight')

