# based on example from: https://scikit-learn.org/stable/auto_examples/svm/plot_svm_margin.html
import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm
from sklearn.datasets import make_blobs

X, y = make_blobs(n_samples=1000, centers=2, n_features=2, random_state=13)
x1 = X[:, 0]
x2 = X[:, 1]

x1_0 = []
x1_1 = []
for i in range(len(x1)):
    if y[i] == 0:
        x1_0.append(x1[i])
    if y[i] == 1:
        x1_1.append(x1[i])

x2_0 = []
x2_1 = []
for i in range(len(x2)):
    if y[i] == 0:
        x2_0.append(x2[i])
    if y[i] == 1:
        x2_1.append(x2[i])

clf = svm.SVC(kernel="linear")
clf.fit(X, y)

w = clf.coef_[0]
a = -w[0] / w[1]
xx = np.linspace(2.3, 9.1)
yy = a * xx - (clf.intercept_[0]) / w[1]

margin = 1 / np.sqrt(np.sum(clf.coef_ ** 2))
yy_down = yy - np.sqrt(1 + a ** 2) * margin
yy_up = yy + np.sqrt(1 + a ** 2) * margin

plt.plot(xx, yy, "k-")
plt.plot(xx, yy_down, "k--")
plt.plot(xx, yy_up, "k--")

plt.scatter(clf.support_vectors_[:, 0][0], clf.support_vectors_[:, 1][0], s=80, zorder=10, marker='o', edgecolors="k", c='b')
plt.scatter(clf.support_vectors_[:, 0][1], clf.support_vectors_[:, 1][1], s=80, zorder=10, marker='o', edgecolors="k", c='b')
plt.scatter(clf.support_vectors_[:, 0][2], clf.support_vectors_[:, 1][2], s=80, zorder=10, marker='<', edgecolors="k", c='r')
plt.scatter(x1_0, x2_0, c='b', marker='o', zorder=10, edgecolors="k")
plt.scatter(x1_1, x2_1, c='r', marker='<', zorder=10, edgecolors="k")

plt.xticks([])
plt.yticks([])
plt.title('Linearly separable data with SVM')
plt.style.use('plot_style.txt')
#plt.show()
plt.savefig('Ball-Rague-Fig8.15.part.eps', bbox_inches='tight')

