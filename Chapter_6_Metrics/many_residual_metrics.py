import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import numpy as np
import math

def adjusted_r2_score(the_data, model, number_of_variables):
    n = len(the_data)
    p = number_of_variables
    return 1 - (1 - r2_score(y_true=the_data, y_pred=model)) * (n - 1) / (n - p - 1)

X_values = np.arange(1, 8)

data = [1, 2.5, 2.9, 6, 3.8, 4.1, 8.2]

model1 = np.arange(1, 8)
model2 = np.arange(0, 7, 1.1)
model3 = np.arange(1.5, 9, 1.15)

number_of_variables_in_model = 1

model1_label = f'MSE ({mean_squared_error(y_true=data, y_pred=model1):.2f}), ' \
               f'RMSE ({math.sqrt(mean_squared_error(y_true=data, y_pred=model1)):.2f}), ' \
               f'MAE ({mean_absolute_error(y_true=data, y_pred=model1):.2f}), ' \
               f'R2 ({r2_score(y_true=data, y_pred=model1):.2f}), ' \
               f'Adjusted R2 ({adjusted_r2_score(data, model1, number_of_variables_in_model):.2f})'
model2_label = f'MSE ({mean_squared_error(y_true=data, y_pred=model2):.2f}), ' \
               f'RMSE ({math.sqrt(mean_squared_error(y_true=data, y_pred=model2)):.2f}), ' \
               f'MAE ({mean_absolute_error(y_true=data, y_pred=model2):.2f}), ' \
               f'R2 ({r2_score(y_true=data, y_pred=model2):.2f}), ' \
               f'Adjusted R2 ({adjusted_r2_score(data, model2, number_of_variables_in_model):.2f})'
model3_label = f'MSE ({mean_squared_error(y_true=data, y_pred=model3):.2f}), ' \
               f'RMSE ({math.sqrt(mean_squared_error(y_true=data, y_pred=model3)):.2f}), ' \
               f'MAE ({mean_absolute_error(y_true=data, y_pred=model3):.2f}), ' \
               f'R2 ({r2_score(y_true=data, y_pred=model3):.2f}), ' \
               f'Adjusted R2 ({adjusted_r2_score(data, model3, number_of_variables_in_model):.2f})'

plt.figure(figsize=(9,5))
plt.plot(X_values, model1, c='green', label=model1_label)  # the model
plt.plot(X_values, model2, c='blue', label=model2_label)  # the model
plt.plot(X_values, model3, c='orange', label=model3_label)  # the model
plt.scatter(X_values, data, c='red')  # the actual data
plt.title(f'Regression Metrics Example')
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
plt.legend()

#plt.show()
plt.savefig('Ball-Rague-Fig6.9.eps', bbox_inches='tight')

