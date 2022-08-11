from sklearn.linear_model import LinearRegression
import random
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error, r2_score

X = []
y = []
random.seed(13)  # set seed to be able to recreate same data

# the same data from the first figure in chapter 8:
for i in range(100):
    temp_x = random.randint(-40, 40)
    X.append(temp_x)
    y.append(temp_x + random.randint(-15, 15))

classifier = LinearRegression()  # create the classifier

# LinearRegression is expecting X to be a matrix.
# Since it is not, we reshape it to match expected shape.
classifier.fit(np.array(X).reshape(-1, 1), y)  # Train the model

print(f'sklearn results: Y = {classifier.intercept_:.2f} + {classifier.coef_[0]:.2f}X ')

y_hat = np.mean(y)
x_hat = np.mean(X)

b_numerator = 0
b_denominator = 0
for i in range(len(X)):
    b_numerator += (X[i] - x_hat) * (y[i] - y_hat)
    b_denominator += (X[i] - x_hat) ** 2

b = b_numerator / b_denominator
a = y_hat - b * x_hat
print(f'Example results: Y = {a:.2f} + {b:.2f}X ')
