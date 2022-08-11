import pandas as pd
import matplotlib.pyplot as plt
#import seaborn as sns

df = pd.read_csv('Titanic_Passengers.csv')
contingency_table = pd.crosstab(df['Gender'], df['Lived_Died'], margins=True) # 'margins=True' shows the summary information

femalecount = contingency_table.iloc[0][0:2].values
malecount = contingency_table.iloc[1][0:2].values
fig = plt.figure(figsize=(8, 4))
#sns.set(font_scale=1.8)
categories = ['Died', 'Survived']
p1 = plt.bar(categories, malecount, color='#d62728')
p2 = plt.bar(categories, femalecount, bottom=malecount)
plt.legend((p2[0], p1[0]), ('Female', 'Male'))
plt.ylabel('Count')

#plt.show()
plt.savefig('Ball-Rague-Fig5.1.eps', bbox_inches='tight')

