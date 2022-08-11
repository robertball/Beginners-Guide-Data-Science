from sklearn import svm
from sklearn.datasets import make_moons, make_circles, make_blobs, make_checkerboard
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
import random

random.seed(13)

X, labels = make_moons(n_samples=1000, noise=0.1, random_state=13)
ss = StandardScaler()
X = ss.fit_transform(X)

x = X[:, 0]
y = X[:, 1]

x_0 = []
x_1 = []
for i in range(len(x)):
    if labels[i] == 0:
        x_0.append(x[i])
    if labels[i] == 1:
        x_1.append(x[i])

y_0 = []
y_1 = []
for i in range(len(y)):
    if labels[i] == 0:
        y_0.append(y[i])
    if labels[i] == 1:
        y_1.append(y[i])

classifier = svm.SVC(kernel='linear')  # possible kernels = linear’, ‘poly’, ‘rbf’, ‘sigmoid’, ‘precomputed’
X_train, X_test, y_train, y_test = train_test_split(X, labels, random_state=13)
classifier.fit(X_train, y_train)
y_preds = classifier.predict(X_test)
linear_accuracy = accuracy_score(y_preds, y_test)

classifier = svm.SVC(kernel='rbf')  # possible kernels = linear’, ‘poly’, ‘rbf’, ‘sigmoid’, ‘precomputed’
classifier.fit(X_train, y_train)
y_preds = classifier.predict(X_test)
rbf_accuracy = accuracy_score(y_preds, y_test)

classifier = svm.SVC(kernel='poly')  # possible kernels = linear’, ‘poly’, ‘rbf’, ‘sigmoid’, ‘precomputed’
classifier.fit(X_train, y_train)
y_preds = classifier.predict(X_test)
poly_accuracy = accuracy_score(y_preds, y_test)

classifier = svm.SVC(kernel='sigmoid')  # possible kernels = linear’, ‘poly’, ‘rbf’, ‘sigmoid’, ‘precomputed’
classifier.fit(X_train, y_train)
y_preds = classifier.predict(X_test)
sigmoid_accuracy = accuracy_score(y_preds, y_test)

plt.figure(figsize=(19, 9))
plt.subplot(2, 2, 1)
plt.scatter(x_0, y_0, c='b', marker='P')
plt.scatter(x_1, y_1, c='r', marker='<')
plt.title(f'kernel accuracies: linear ({(linear_accuracy*100):.2f}%), rbf({(rbf_accuracy*100):.2f}%), poly({(poly_accuracy*100):.2f}%), sigmoid({(sigmoid_accuracy*100):.2f}%)')

X, labels = make_circles(n_samples=1000, noise=0.05, random_state=13)
ss = StandardScaler()
X = ss.fit_transform(X)
x = X[:, 0]
y = X[:, 1]

x_0 = []
x_1 = []
for i in range(len(x)):
    if labels[i] == 0:
        x_0.append(x[i])
    if labels[i] == 1:
        x_1.append(x[i])

y_0 = []
y_1 = []
for i in range(len(y)):
    if labels[i] == 0:
        y_0.append(y[i])
    if labels[i] == 1:
        y_1.append(y[i])

classifier = svm.SVC(kernel='linear')  # possible kernels = linear’, ‘poly’, ‘rbf’, ‘sigmoid’, ‘precomputed’
X_train, X_test, y_train, y_test = train_test_split(X, labels, random_state=13)
classifier.fit(X_train, y_train)
y_preds = classifier.predict(X_test)
linear_accuracy = accuracy_score(y_preds, y_test)

classifier = svm.SVC(kernel='rbf')  # possible kernels = linear’, ‘poly’, ‘rbf’, ‘sigmoid’, ‘precomputed’
classifier.fit(X_train, y_train)
y_preds = classifier.predict(X_test)
rbf_accuracy = accuracy_score(y_preds, y_test)

classifier = svm.SVC(kernel='poly')  # possible kernels = linear’, ‘poly’, ‘rbf’, ‘sigmoid’, ‘precomputed’
classifier.fit(X_train, y_train)
y_preds = classifier.predict(X_test)
poly_accuracy = accuracy_score(y_preds, y_test)

classifier = svm.SVC(kernel='sigmoid')  # possible kernels = linear’, ‘poly’, ‘rbf’, ‘sigmoid’, ‘precomputed’
classifier.fit(X_train, y_train)
y_preds = classifier.predict(X_test)
sigmoid_accuracy = accuracy_score(y_preds, y_test)

plt.subplot(2, 2, 2)
plt.scatter(x_0, y_0, c='b', marker='P')
plt.scatter(x_1, y_1, c='r', marker='<')
plt.title(f'kernel accuracies: linear ({(linear_accuracy*100):.2f}%), rbf({(rbf_accuracy*100):.2f}%), poly({(poly_accuracy*100):.2f}%), sigmoid({(sigmoid_accuracy*100):.2f}%)')

X, labels = make_blobs(n_samples=1000, centers=2, n_features=2, random_state=13)
x = X[:, 0]
y = X[:, 1]

x_0 = []
x_1 = []
for i in range(len(x)):
    if labels[i] == 0:
        x_0.append(x[i])
    if labels[i] == 1:
        x_1.append(x[i])

y_0 = []
y_1 = []
for i in range(len(y)):
    if labels[i] == 0:
        y_0.append(y[i])
    if labels[i] == 1:
        y_1.append(y[i])

classifier = svm.SVC(kernel='linear')  # possible kernels = linear’, ‘poly’, ‘rbf’, ‘sigmoid’, ‘precomputed’
X_train, X_test, y_train, y_test = train_test_split(X, labels, random_state=13)
classifier.fit(X_train, y_train)
y_preds = classifier.predict(X_test)
linear_accuracy = accuracy_score(y_preds, y_test)

classifier = svm.SVC(kernel='rbf')  # possible kernels = linear’, ‘poly’, ‘rbf’, ‘sigmoid’, ‘precomputed’
classifier.fit(X_train, y_train)
y_preds = classifier.predict(X_test)
rbf_accuracy = accuracy_score(y_preds, y_test)

classifier = svm.SVC(kernel='poly')  # possible kernels = linear’, ‘poly’, ‘rbf’, ‘sigmoid’, ‘precomputed’
classifier.fit(X_train, y_train)
y_preds = classifier.predict(X_test)
poly_accuracy = accuracy_score(y_preds, y_test)

classifier = svm.SVC(kernel='sigmoid')  # possible kernels = linear’, ‘poly’, ‘rbf’, ‘sigmoid’, ‘precomputed’
classifier.fit(X_train, y_train)
y_preds = classifier.predict(X_test)
sigmoid_accuracy = accuracy_score(y_preds, y_test)

plt.subplot(2, 2, 3)
plt.scatter(x_0, y_0, c='b', marker='P')
plt.scatter(x_1, y_1, c='r', marker='<')
plt.title(f'kernel accuracies: linear ({(linear_accuracy*100):.2f}%), rbf({(rbf_accuracy*100):.2f}%), poly({(poly_accuracy*100):.2f}%), sigmoid({(sigmoid_accuracy*100):.2f}%)')

x = []
y = []
labels = [0]*500
labels.extend([1]*500)
for i in range(1000):
    x.append(random.uniform(-1, 1))
    y.append(random.uniform(-1, 1))

x_0 = []
x_1 = []
for i in range(len(x)):
    if labels[i] == 0:
        x_0.append(x[i])
    if labels[i] == 1:
        x_1.append(x[i])

y_0 = []
y_1 = []
for i in range(len(y)):
    if labels[i] == 0:
        y_0.append(y[i])
    if labels[i] == 1:
        y_1.append(y[i])

classifier = svm.SVC(kernel='linear')  # possible kernels = linear’, ‘poly’, ‘rbf’, ‘sigmoid’, ‘precomputed’
X_train, X_test, y_train, y_test = train_test_split(X, labels, random_state=13)
classifier.fit(X_train, y_train)
y_preds = classifier.predict(X_test)
linear_accuracy = accuracy_score(y_preds, y_test)

classifier = svm.SVC(kernel='rbf')  # possible kernels = linear’, ‘poly’, ‘rbf’, ‘sigmoid’, ‘precomputed’
classifier.fit(X_train, y_train)
y_preds = classifier.predict(X_test)
rbf_accuracy = accuracy_score(y_preds, y_test)

classifier = svm.SVC(kernel='poly')  # possible kernels = linear’, ‘poly’, ‘rbf’, ‘sigmoid’, ‘precomputed’
classifier.fit(X_train, y_train)
y_preds = classifier.predict(X_test)
poly_accuracy = accuracy_score(y_preds, y_test)

classifier = svm.SVC(kernel='sigmoid')  # possible kernels = linear’, ‘poly’, ‘rbf’, ‘sigmoid’, ‘precomputed’
classifier.fit(X_train, y_train)
y_preds = classifier.predict(X_test)
sigmoid_accuracy = accuracy_score(y_preds, y_test)

plt.subplot(2, 2, 4)
#plt.scatter(x, y, c=labels, cmap='bwr')
plt.scatter(x_0, y_0, c='b', marker='P')
plt.scatter(x_1, y_1, c='r', marker='<')
plt.title(f'kernel accuracies: linear ({(linear_accuracy*100):.2f}%), rbf({(rbf_accuracy*100):.2f}%), poly({(poly_accuracy*100):.2f}%), sigmoid({(sigmoid_accuracy*100):.2f}%)')
plt.suptitle("Comparison of different datasets and accuracies for various kernels with SVM")
plt.subplots_adjust(left=0.1,
                    bottom=0.1, 
                    right=0.9, 
                    top=0.9, 
                    wspace=0.20, 
                    hspace=0.25)

#plt.style.use('plot_style.txt')
#plt.show()
plt.savefig('Ball-Rague-Fig8.16.eps', bbox_inches='tight')
