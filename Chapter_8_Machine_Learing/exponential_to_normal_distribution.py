from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import QuantileTransformer
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import boxcox
from sklearn.metrics import mean_squared_error

np.random.seed(13)

y = sorted(np.random.exponential(scale=10, size=1000))

x_axis = np.arange(len(y))

classifier = LinearRegression()  # create the classifier
classifier.fit(np.array(x_axis).reshape(-1, 1), y)  # Train the model

fig, axs = plt.subplots(2, 2, figsize=(7.5, 6.5))

axs[0, 0].scatter(x_axis, y)
y_preds = classifier.predict(np.array(x_axis).reshape(-1, 1))
axs[0, 0].plot(x_axis, y_preds, c='red')
axs[0, 0].set_title(f'Exponential Data MSE({mean_squared_error(y, y_preds):.2f})', fontsize=9)
ax[0, 0].tick_params(axis='both', which='major', labelsize=2)

# find the best lambda for this dataset (quick hypertuning):
minimized_error = np.inf
new_lambda = -0.5
for i in np.arange(-0.5, 0.5, 0.001):
    y_boxcox = boxcox(y, lmbda=i)
    classifier.fit(np.array(x_axis).reshape(-1, 1), y_boxcox)  # Train the model
    y_preds = classifier.predict(np.array(x_axis).reshape(-1, 1))
    mse = mean_squared_error(y_boxcox, y_preds)
    if mse < minimized_error:
        minimized_error = mse
        new_lambda = i

y_boxcox = boxcox(y, lmbda=new_lambda)
axs[0, 1].scatter(x_axis, y_boxcox)
classifier.fit(np.array(x_axis).reshape(-1, 1), y_boxcox)  # Train the model
y_preds = classifier.predict(np.array(x_axis).reshape(-1, 1))
axs[0, 1].plot(x_axis, y_preds, c='red')
axs[0, 1].set_title(f'Box-Cox Transformation MSE({mean_squared_error(y_boxcox, y_preds):.2f})', fontsize=9)

qt = QuantileTransformer(output_distribution='normal')
y_normal = qt.fit_transform(np.array(y).reshape(-1, 1))
axs[1, 0].scatter(x_axis, y_normal)
classifier.fit(np.array(x_axis).reshape(-1, 1), y_normal)  # Train the model
y_preds = classifier.predict(np.array(x_axis).reshape(-1, 1))
axs[1, 0].plot(x_axis, y_preds, c='red')
axs[1, 0].set_title(f'QuantileTransformer Transformation MSE({mean_squared_error(y_normal, y_preds):.2f})', fontsize=9)

y_log = np.log(y)
axs[1, 1].scatter(x_axis, y_log)
classifier.fit(np.array(x_axis).reshape(-1, 1), y_log)  # Train the model
y_preds = classifier.predict(np.array(x_axis).reshape(-1, 1))
axs[1, 1].plot(x_axis, y_preds, c='red')
axs[1, 1].set_title(f'Log Transformation MSE({mean_squared_error(y_log, y_preds):.2f})', fontsize=9)

plt.suptitle('Various Example Transformations')
plt.rc('font', size=1)
plt.subplots_adjust(left=0.1,
                    bottom=0.1, 
                    right=0.9, 
                    top=0.9, 
                    wspace=0.40, 
                    hspace=0.25)

#plt.show()
plt.savefig('Ball-Rague-Fig8.12.eps', bbox_inches='tight')
