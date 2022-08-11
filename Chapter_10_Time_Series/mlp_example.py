import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from numpy.lib.stride_tricks import sliding_window_view
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error
from sklearn.neural_network import MLPRegressor
from sklearn.metrics import mean_squared_error

# This file uses sliding_window_view, which provides a quick and easy way of making sliding windows.
# sliding_window_view(total.flatten(), window_size) is equivalent (except that it is a view, which generally conserves memory) of the following:
# X_train3 = []
# for i in range(window_size, train_size + window_size):
#     X_train3.append(total[i - window_size:i, 0])
# X_train3 = np.array(X_train3)

df = pd.read_csv('US_energy_consumption_1973_to_Jul_2021.csv', parse_dates=['Date'], index_col=['Date'])

sc = StandardScaler()  # neural networks require scaling
total = sc.fit_transform(np.array(df['total']).reshape(-1, 1))

train_size = 466  # 466 is 80% training set

# # using 80/20 split:
X_train = np.arange(0, train_size).reshape(-1, 1)
y_train = total[:train_size].flatten()
X_test = np.arange(train_size, 583).reshape(-1, 1)
y_test = total[train_size:].flatten()

# Traditionally, you just use fit and predict with the 80/20 split.
# This does not work, all it does is provide a trend line:
# mlp = MLPRegressor(random_state=13).fit(X_train, y_train)
# predicted_80_20 = mlp.predict(X_test)

# Using walk forward validation with time step:
time_step_walk_forward_predictions = []
for i in X_test:
    print(f'Time Step Walk Forward, i = {i[0]}')
    X_train2 = np.arange(0, i[0]).reshape(-1, 1)  # change the training range - expanding window
    y_train2 = total[:i[0]].flatten()  # change the training range - expanding window
    mlp = MLPRegressor(random_state=13).fit(X_train2, y_train2)  # retrain - sklearn does not provide a way to update a neural network
    time_step_walk_forward_predictions.append(mlp.predict([i])[0])

plt.subplots(figsize=(10,5))
plt.subplot(1, 2, 1)
plt.plot(X_train, y_train, label='Train')
plt.plot(X_test, y_test, label='Test')
plt.plot(X_test, time_step_walk_forward_predictions, label=f'Time Step MSE={mean_squared_error(y_test, time_step_walk_forward_predictions):.3f}')
plt.title('Time Step Walk Forward')
plt.legend(fontsize=6)
plt.gca().xaxis.set_major_locator(plt.NullLocator())  # remove x ticks
plt.gca().yaxis.set_major_locator(plt.NullLocator())  # remove y ticks

# using walk forward with windowing:
plt.subplot(1, 2, 2)
plt.plot(X_train, y_train, label='Train')
plt.plot(X_test, y_test, label='Test')

window_sizes = [1, 12, 25]
for window_size in window_sizes:
    walk_forward_predictions_windowing = []
    print(f'Window size = {window_size}.')
    for i in range(len(X_test)):
        print(f'Windowing Walk Forward i = {i}')
        X_train4 = sliding_window_view(total[:train_size+i].flatten(), window_size)
        y_train4 = total[window_size:train_size+i+1].flatten()
        mlp = MLPRegressor(random_state=13).fit(X_train4, y_train4)
        input_window = X_train4[-1]  # a sliding window is needed as input. First, copy the last sliding window from the X_train4 data
        input_window = np.delete(input_window, 0)  # Next, delete the first entry because we need to shift forward in time. (The code is equivalent to input_window.pop(0), if it were a list.)
        input_window = np.append(input_window, y_train4[-1])  # Last, we finish the shift by appending the last value that was just used for training.
        walk_forward_predictions_windowing.append(mlp.predict([input_window])[0])

    plt.plot(X_test, walk_forward_predictions_windowing, label=f'Windowing size={window_size} MSE={mean_squared_error(y_test, walk_forward_predictions_windowing):.3f}')

plt.title('Windowing Walk Forward')
plt.legend(fontsize=6)
plt.gca().xaxis.set_major_locator(plt.NullLocator())  # remove x ticks
plt.gca().yaxis.set_major_locator(plt.NullLocator())  # remove y ticks

plt.suptitle('MLP (Multi-Level Perceptron) Time Step vs Windowing Comparison')

#plt.show()
plt.savefig('Ball-Rague-Fig10.17.eps', bbox_inches='tight')
