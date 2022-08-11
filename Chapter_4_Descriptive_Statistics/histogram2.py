import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

iris_df = pd.read_csv('iris.csv')

ax = sns.distplot(iris_df['petal_length'], color=(0.643137254901961, 0.784313725490196, 0.87843137254902))
ax = sns.distplot(iris_df['petal_length'], hist=None, color=(0.145098039215686, 0.462745098039216, 0.682352941176471))  # color='blue')
ax.set_title('Distribution of Petal Length')
ax.set_xlabel('Petal Length (cm)')

#plt.show()
plt.savefig('Ball-Rague-Fig4.6.eps', bbox_inches='tight')

