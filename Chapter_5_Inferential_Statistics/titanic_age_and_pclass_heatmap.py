import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from sklearn import preprocessing

plt.rc('font', size=7)
#sns.set(style="ticks", color_codes=True)
#sns.set(font_scale=1.5)  # make the text bigger

df = pd.read_csv('Titanic_Passengers.csv')

df = df.drop(columns=['Name', 'Born', 'Died', 'Fare', 'Fare_decimal'])
df = df.dropna()
df.rename(columns={'Passenger_Class': 'Passenger Class'}, inplace=True)  # rename Passenger_Class to Passenger Class so that it looks nicer for the image

le = preprocessing.LabelEncoder()

df['Lived_Died_int'] = le.fit_transform(df['Lived_Died'])

df['Age Bins'] = pd.cut(x=df['Age'], bins=[0, 9, 19, 29, 39, 49, 59, 69, 79])

table = pd.pivot_table(df, values='Lived_Died_int', index=['Gender'], columns=['Passenger Class', 'Age Bins'])

table.applymap(lambda x: 1 - x)  # the results are inverted for the heatmap

xlabels = ['PC 1: 0-9', 'PC 1: 10-19', 'PC 1: 20-29', 'PC 1: 30-39', 'PC 1: 40-49', 'PC 1: 50-59', 'PC 1: 60-69', 'PC 1: 70-∞',
           'PC 2: 0-9', 'PC 2: 10-19', 'PC 2: 20-29', 'PC 2: 30-39', 'PC 2: 40-49', 'PC 2: 50-59', 'PC 2: 60-69', 'PC 2: 70-∞',
           'PC 3: 0-9', 'PC 3: 10-19', 'PC 3: 20-29', 'PC 3: 30-39', 'PC 3: 40-49', 'PC 3: 50-59', 'PC 3: 60-69', 'PC 3: 70-∞']
plt.figure(figsize=(11,5))
#ax = plt.axes()
plt.suptitle("Heatmap Comparing Age and Gender")
sns.heatmap(table, annot=True, yticklabels=['Female', 'Male'], xticklabels=xlabels, fmt='.2f')

#plt.show()
plt.savefig('Ball-Rague-Fig5.5.eps', bbox_inches='tight')

