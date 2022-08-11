import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv('iris.csv')
sns.pairplot(df, hue='class', height=1.45)
#plt.show()
plt.savefig('Ball-Rague-Fig4.8.eps', bbox_inches='tight')

