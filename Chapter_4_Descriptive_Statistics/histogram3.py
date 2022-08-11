import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv('iris.csv')

setosa = df[df['class'] == 'Iris-setosa']
versicolor = df[df['class'] == 'Iris-versicolor']
virginica = df[df['class'] == 'Iris-virginica']

ax = sns.distplot(setosa['petal_length'], label='Iris Setosa', color=(0.643137254901961, 0.784313725490196, 0.87843137254902))
ax = sns.distplot(setosa['petal_length'], hist=None, color=(0.145098039215686, 0.462745098039216, 0.666666666666667))
ax = sns.distplot(versicolor['petal_length'], label='Iris Versicolor', color=(1, 0.792156862745098, 0.619607843137255))
ax = sns.distplot(versicolor['petal_length'], hist=None, color=(0.968627450980392, 0.552941176470588, 0.145098039215686))
ax = sns.distplot(virginica['petal_length'], label='Iris Virginica', color=(0.666666666666667, 0.854901960784314, 0.666666666666667))
ax = sns.distplot(virginica['petal_length'], hist=None, color=(0.219607843137255, 0.611764705882353, 0.215686274509804))
ax.set_title('Distribution of Petal Length')
ax.set_xlabel('Petal Length (cm)')
plt.legend()

#plt.show()
plt.savefig('Ball-Rague-Fig4.7.eps', bbox_inches='tight')

