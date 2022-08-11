from sklearn import datasets
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split, cross_val_score
import numpy as np

iris = datasets.load_iris()
tree = DecisionTreeClassifier()

X = iris.data
y = iris.target
rs = np.random.seed(13)
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=rs)

tree.fit(X_train, y_train)
y_pred = tree.predict(X_test)

print(f'Traditional Hold Out Accuracy = {(accuracy_score(y_test, y_pred)*100):.2f}%.')

result = cross_val_score(tree, X, y)  # defaults to 5 folds

print(f'5-fold Cross Validation Average Accuracy: {(result.mean())*100:.2f}%.')
