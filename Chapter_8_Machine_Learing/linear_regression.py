from sklearn.linear_model import LinearRegression
import random
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error, r2_score

X = []
y = []
random.seed(13)  # set seed to be able to recreate image

# the same data from Figure 58 in chapter 8:
for i in range(100):
    x = random.randint(-40, 40)
    X.append(x)
    y.append(x + random.randint(-15, 15))

classifier = LinearRegression()  # create the classifier

# LinearRegression is expecting X to be a matrix.
# Since it is not, we reshape it to match expected shape.
classifier.fit(np.array(X).reshape(-1, 1), y)  # Train the model

y_pred = classifier.predict(np.array(X).reshape(-1, 1))

mse = mean_squared_error(y, y_pred)
r2_score = r2_score(y, y_pred)

plt.subplots(figsize=(10,5))
ax1 = plt.subplot(121)
ax1.scatter(X, y)
ax1.plot(X, y_pred, c='red')
plt.xlim(-45, 100)  # have the same X-axis range
plt.ylim(-60, 100)  # have the same Y-axis range

ax2 = plt.subplot(122)
ax2.scatter(X, y)
X.append(100)
y_pred = classifier.predict(np.array(X).reshape(-1, 1))
ax2.plot(X, y_pred, c='red')
plt.xlim(-45, 100)
plt.ylim(-60, 100)
plt.suptitle(f'Linear Regression Example (MSE={mse:.2f}, R2={r2_score:.2f})')

#plt.show()
plt.savefig('Ball-Rague-Fig8.11.eps', bbox_inches='tight')

