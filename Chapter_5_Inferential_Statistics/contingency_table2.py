import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('Titanic_Passengers.csv')
print(pd.crosstab(df['Passenger_Class'], df['Lived_Died'], margins=True))

contingency_table = pd.crosstab(df['Passenger_Class'], df['Lived_Died'], margins=False)

#Assigns the frequency values:
firstClassCount = contingency_table.iloc[0].values
secondClassCount = contingency_table.iloc[1].values
thirdClassCount = contingency_table.iloc[2].values

#Plots the bar chart
fig = plt.figure(figsize=(10, 5))
#sns.set(font_scale=1.8)
categories = ['Died', 'Survived']
p1 = plt.bar(categories, firstClassCount, 0.55, color='#d62728')
p2 = plt.bar(categories, secondClassCount, 0.55, bottom=firstClassCount)
p3 = plt.bar(categories, thirdClassCount, 0.55, bottom=firstClassCount+secondClassCount)
plt.legend((p1[0], p2[0], p3[0]), ('First Class', 'Second Class', 'Third Class'))
plt.ylabel('Count')

#plt.show()
plt.savefig('Ball-Rague-Fig5.4.eps', bbox_inches='tight')

