import numpy as np
from sklearn import svm
from sklearn.datasets import make_moons, make_circles, make_blobs, make_checkerboard
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
import random

rs = random.seed(13)
X, labels = make_moons(n_samples=1000, noise=0.1, random_state=rs)
ss = StandardScaler()
X = ss.fit_transform(X)

possible_C_values = np.arange(0.1, 1.6, 0.1)  # arange provides 15 different values of C from 0.0 to 1.5 with 0.1 steps

# hyperparameters:
parameters = {"kernel": ['linear', 'rbf', 'sigmoid', 'poly'],
              "gamma": ['scale', 'auto'],
              "C": possible_C_values}

clf = GridSearchCV(svm.SVC(), parameters, n_jobs=-1)  # -1 means to use all available CPUs
clf.fit(X=X, y=labels)
svm_model = clf.best_estimator_  # the best trained SVM model

# print out the best score and best parameters:
print(f'Average (mean) r2 scores from cross validation for the best parameters: {clf.best_score_}.')
print(f'Best parameters: {clf.best_params_}')
