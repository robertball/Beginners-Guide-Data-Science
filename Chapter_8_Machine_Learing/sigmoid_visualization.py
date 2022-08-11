import numpy as np
import matplotlib.pyplot as plt


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


sigmoid_v = np.vectorize(sigmoid)  # this allows an array to be processed all at once by the sigmoid function
x_axis = np.arange(-6, 7, 0.1)

plt.plot(x_axis, sigmoid_v(x_axis))
plt.title('Sigmoid Function')
plt.yticks([0, 0.25, 0.5, 0.75, 1.0])
plt.ylabel('Probability')
plt.grid(True)
#plt.show()
plt.style.use('plot_style.txt')
plt.savefig('Ball-Rague-Fig8.14.eps', bbox_inches='tight')
