import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from sklearn import preprocessing

df = pd.read_csv('Titanic_Passengers.csv')

df = df.drop(columns=['Name', 'Born', 'Died', 'Fare', 'Fare_decimal', 'Passenger_Class'])
df = df.dropna()

le = preprocessing.LabelEncoder()

df['Lived_Died_int'] = le.fit_transform(df['Lived_Died'])

df['Age Bins'] = pd.cut(x=df['Age'], bins=[0, 9, 19, 29, 39, 49, 59, 69, 79])

table = pd.pivot_table(df, values='Lived_Died_int', index=['Gender'], columns=['Age Bins'])

table.applymap(lambda x: 1 - x)  # the results are inverted for the heatmap

xlabels = ['0-9', '10-19', '20-29', '30-39', '40-49', '50-59', '60-69', '70-∞']
#ax = plt.axes(figsize=(10,5))
fig = plt.figure(figsize=(10,5))
sns.heatmap(table, annot=True, yticklabels=['Female', 'Male'], xticklabels=xlabels, fmt='.2f')
fig.suptitle("Heatmap Comparing Age and Gender")
plt.xticks(rotation=90) 

#plt.show()
plt.savefig('Ball-Rague-Fig5.3.eps', bbox_inches='tight')

