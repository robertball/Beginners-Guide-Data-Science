#  Visualization of logistic regression based on, but modified from: https://favtutor.com/blogs/decision-boundary-logistic-regression
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.decomposition import PCA
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score

df = pd.read_csv('iris.csv')

X = StandardScaler().fit_transform(df.iloc[:, 0:3])
y = LabelEncoder().fit_transform(df['class'])

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=13)

# for accuracy:
clf = LogisticRegression()
model = clf.fit(X_train, y_train)
y_pred = model.predict(X_test)

# for the visualization:
pca = PCA(n_components=2)
X_train_pca = pca.fit_transform(X_train)
X_test_pca = pca.transform(X_test)

clf = LogisticRegression()
model = clf.fit(X_train_pca, y_train)

# The following is needed to create the contours in the visualization:
x_min, x_max = X_train_pca[:, 0].min() - 1, X_train_pca[:, 0].max() + 1
y_min, y_max = X_train_pca[:, 1].min() - 1, X_train_pca[:, 1].max() + 1
xx_train, yy_train = np.meshgrid(np.arange(x_min, x_max, 0.1), np.arange(y_min, y_max, 0.1))
Z_train = model.predict(np.c_[xx_train.ravel(), yy_train.ravel()])
Z_train = Z_train.reshape(xx_train.shape)
x_min, x_max = X_test_pca[:, 0].min() - 1, X_test_pca[:, 0].max() + 1
y_min, y_max = X_test_pca[:, 1].min() - 1, X_test_pca[:, 1].max() + 1
xx_test, yy_test = np.meshgrid(np.arange(x_min, x_max, 0.1), np.arange(y_min, y_max, 0.1))
Z_test = model.predict(np.c_[xx_test.ravel(), yy_test.ravel()])
Z_test = Z_test.reshape(xx_test.shape)

X_train_0 = []
X_train_1 = []
X_train_2 = []
for i in range(len(X_train_pca)):
    if y_train[i] == 0:
        X_train_0.append(X_train_pca[i])
    if y_train[i] == 1:
        X_train_1.append(X_train_pca[i])
    if y_train[i] == 2:
        X_train_2.append(X_train_pca[i])

X_train_0 = np.array(X_train_0)
X_train_1 = np.array(X_train_1)
X_train_2 = np.array(X_train_2)

X_test_0 = []
X_test_1 = []
X_test_2 = []
for i in range(len(X_test_pca)):
    if y_test[i] == 0:
        X_test_0.append(X_test_pca[i])
    if y_test[i] == 1:
        X_test_1.append(X_test_pca[i])
    if y_test[i] == 2:
        X_test_2.append(X_test_pca[i])

X_test_0 = np.array(X_test_0)
X_test_1 = np.array(X_test_1)
X_test_2 = np.array(X_test_2)

plt.figure(figsize=(20, 6))
plt.subplot(1, 2, 1)
plt.contour(xx_train, yy_train, Z_train, cmap='RdYlBu')
plt.scatter(X_train_0[:, 0], X_train_0[:, 1], marker='o', c='r', s=30, edgecolor='k')
plt.scatter(X_train_1[:, 0], X_train_1[:, 1], marker='P', c='y', s=30, edgecolor='k')
plt.scatter(X_train_2[:, 0], X_train_2[:, 1], marker='>', c='b', s=30, edgecolor='k')
plt.title('Scatter Plot with Decision Boundary for the Training Set')
plt.xticks([])
plt.yticks([])
plt.subplot(1, 2, 2)
plt.contour(xx_test, yy_test, Z_test, cmap='RdYlBu')
plt.scatter(X_test_0[:, 0], X_test_0[:, 1], marker='o', c='r', s=30, edgecolor='k')
plt.scatter(X_test_1[:, 0], X_test_1[:, 1], marker='P', c='y', s=30, edgecolor='k')
plt.scatter(X_test_2[:, 0], X_test_2[:, 1], marker='>', c='b', s=30, edgecolor='k')
plt.title('Scatter Plot with Decision Boundary for the Test Set')
plt.xticks([])
plt.yticks([])
plt.suptitle(f'Visualization of Logistic Regression Boundaries with Iris Dataset, Accuracy={(accuracy_score(y_test, y_pred)*100):.2f}%')

plt.style.use('plot_style.txt')
#plt.show()
plt.savefig('Ball-Rague-Fig8.13.eps', bbox_inches='tight')
