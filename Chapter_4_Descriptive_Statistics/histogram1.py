import pandas as pd
import matplotlib.pyplot as plt  # this is needed to show visual charts

iris_df = pd.read_csv('iris.csv')
ax = iris_df['petal_length'].plot.hist()
ax.set_title('Distribution of Petal Length')
#plt.show()
plt.savefig('Ball-Rague-Fig4.5.eps', bbox_inches='tight')


