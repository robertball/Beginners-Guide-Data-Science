import pandas as pd
import matplotlib.pyplot as plt

iris_df = pd.read_csv('iris.csv')

plt.figure(figsize=(10, 5))
iris_df.boxplot()

#plt.show()
plt.savefig('Ball-Rague-Fig4.4.eps', bbox_inches='tight')


