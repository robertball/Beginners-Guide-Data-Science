import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('iris.csv')

correlation_table = df.corr(method='pearson')
plt.figure(figsize=(9,3))
ax = sns.heatmap(correlation_table, vmin=-1, vmax=1, annot=True)
ax.set_title("Correlation Table for Iris Data")

ax.set_yticklabels(['Sepal Length', 'Sepal Width', 'Petal Length', 'Petal Width'], fontdict={'verticalalignment': 'center'}, rotation=0)  # make the yticks pretty
ax.set_xticklabels(['Sepal Length', 'Sepal Width', 'Petal Length', 'Petal Width'])  # make the xticks pretty

#plt.show()
plt.savefig('Ball-Rague-Fig4.17.eps', bbox_inches='tight')

