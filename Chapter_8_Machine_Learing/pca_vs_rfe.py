import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.feature_selection import RFE
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn import tree
from sklearn import preprocessing
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('penguins_no_nulls.csv', index_col='Sample Number')  # load the data

le = preprocessing.LabelEncoder()  # create the object
df = df.apply(le.fit_transform)  # transforms all strings to ints

features = df.columns[0:len(df.columns)-1]  # get all the features' names except the classification
np_features = np.array(features)  # for RFE for filtering with Boolean lists

# standard practice: break the dataset apart into test/train for predictions:
X = df.iloc[:, 0:len(df.columns)-1].values  # values of the features except for 'Species'
y = df.iloc[:, len(df.columns)-1].values  # the values we are trying to predict ('Species')

# random_state=0 is so that the data is split the same way each time so it matches the example in the book:
rs = np.random.seed(0)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=rs)

# we have to scale for PCA:
sc = StandardScaler()
scaled_X_train = sc.fit_transform(X_train)
# only transform the X_test data. We don't 'learn' (fit) from the test data because that would be cheating
# in other words, we use 'transform' instead of 'fit_transform'.
# The idea is to blindly transform the test data based on the training data.
scaled_X_test = sc.transform(X_test)

classifier = tree.DecisionTreeClassifier()  # the classifier
classifier.fit(X_train, y_train)  # this is not using the scaled data
y_pred = classifier.predict(X_test)  # this is not using the scaled data

print(f"X_train.columns = {X_train.shape}")
print(f"With all the features (14): {accuracy_score(y_test, y_pred)}")

PCA_accuracy = [accuracy_score(y_test, y_pred)]
RFE_accuracy = [accuracy_score(y_test, y_pred)]

for num_components_features in range(len(df.columns)-2, 0, -1):
    pca = PCA(n_components=num_components_features)
    PCA_X_train = pca.fit_transform(scaled_X_train)
    # once again, notice that with the test data we only use 'tranform', not 'fit_transform.'
    PCA_X_test = pca.transform(scaled_X_test)
    classifier.fit(PCA_X_train, y_train)
    y_pred = classifier.predict(PCA_X_test)
    PCA_accuracy.append(accuracy_score(y_test, y_pred))
    print(f"num_components_features = {num_components_features}, accuracy = {accuracy_score(y_test, y_pred)}")

    rfe = RFE(estimator=classifier, n_features_to_select=num_components_features)
    RFE_X_train = rfe.fit_transform(X_train, y_train)
    RFE_X_test = rfe.transform(X_test)
    classifier.fit(RFE_X_train, y_train)
    y_pred = classifier.predict(RFE_X_test)
    RFE_accuracy.append(accuracy_score(y_test, y_pred))

print(PCA_accuracy)
for i, j in enumerate(PCA_accuracy):
    print(f"{i}, {j}")

plt.title('Accuracy of PCA vs RFE for Palmer Penguins')
plt.plot(PCA_accuracy, '-', label='PCA Accuracy')
plt.plot(RFE_accuracy, '-.', label='RFE Accuracy')
plt.legend()
plt.xticks(ticks=np.arange(len(df.columns)-1), labels=[str(x) for x in np.arange(len(df.columns)-1, 0, -1)])
plt.xlabel('Number of features or components')
plt.ylabel("Accuracy of the decision tree")
#plt.show()
plt.style.use('plot_style.txt')
plt.savefig('Ball-Rague-Fig8.28.eps', bbox_inches='tight')

