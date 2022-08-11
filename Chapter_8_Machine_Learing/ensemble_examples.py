from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.metrics import accuracy_score

iris = load_iris()
X = iris.data
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=13)

random_forest = RandomForestClassifier(random_state=13)
random_forest.fit(X_train, y_train)
y_preds = random_forest.predict(X_test)
print(f'Random forest accuracy = {accuracy_score(y_test, y_preds)*100:.2f}%.')

AdaBoost = AdaBoostClassifier(random_state=13)
AdaBoost.fit(X_train, y_train)
y_preds = AdaBoost.predict(X_test)
print(f'AdaBoost accuracy = {accuracy_score(y_test, y_preds)*100:.2f}%.')

