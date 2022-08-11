import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

df = pd.DataFrame({
    'height': [163, 185, 167, 184, 180, 160, 175, 174],
    'weight': [54, 93, 90, 102, 88, 50, 70, 91],
    'age': [18, 22, 68, 31, 24, 25, 32, 55],
    'iq': [90, 110, 108, 88, 90, 100, 70, 130]
})

# the following will scale all the values
scaled_numpy_array = StandardScaler().fit_transform(df)

# create the PCA object and set it so that it will reduce the features 
# (columns) down to two components:
pca = PCA(n_components=2)
# the result is 8 pairs of components
principal_components = pca.fit_transform(scaled_numpy_array)  

for component1, component2 in principal_components:
    plt.scatter(component1, component2)
plt.xlabel("Component 1")
plt.ylabel("Component 2")
plt.title("PCA (2 components) from 8 people's 4 features")

#plt.show()
plt.savefig('Ball-Rague-Fig8.24.a.eps', bbox_inches='tight')

