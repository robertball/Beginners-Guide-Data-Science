from sklearn import preprocessing, tree
from sklearn.tree import export_text
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('sledding.csv')

df = df.apply(preprocessing.LabelEncoder().fit_transform)  # convert all strings to integers
features = ['snowing', 'temperature', 'wind', 'time']
X = df[features]  # the data
y = df[['predictor(sledding)']]  # the predictor

# print(X)
# print(y)

decision_tree = tree.DecisionTreeClassifier(criterion='entropy')  # 'gini' is the default
decision_tree = decision_tree.fit(X, y)

# print(decision_tree.feature_importances_)

print(export_text(decision_tree, feature_names=features))

fig = plt.figure(figsize=(3.5, 3.8))
#tree.plot_tree(decision_tree, filled=True, feature_names=features)
tree.plot_tree(decision_tree, filled=False, feature_names=features, fontsize=6.5)

#plt.style.use('plot_style.txt')
#plt.rc('font', size=20)
#fig, axes = plt.subplots(nrows = 1,ncols = 1,figsize = (5,5), dpi=300)

plt.savefig('Ball-Rague-Fig8.5.eps', bbox_inches='tight')
#plt.show()
#plt.savefig('decision_tree.png')

print(decision_tree.feature_importances_)

