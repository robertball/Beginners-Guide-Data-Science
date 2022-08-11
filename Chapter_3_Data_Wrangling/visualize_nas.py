import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('royal_line.csv', index_col='ID')
plt.figure(figsize=(9,4))
sns.heatmap(df.isnull(), yticklabels=False, cbar=False)

#plt.show()
plt.savefig('Ball-Rague-Fig3.2.eps', bbox_inches='tight')

