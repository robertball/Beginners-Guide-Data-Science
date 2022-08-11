import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set(style="ticks", color_codes=True)

data = pd.read_csv('Titanic_Passengers.csv')

data = data.drop(columns=['Name', 'Born', 'Died', 'Fare', 'Fare_decimal'])
data = data.dropna()

data.loc[data['Gender'] == 'Female', 'Gender'] = 1
data.loc[data['Gender'] == 'Male', 'Gender'] = 0

data.loc[data['Lived_Died'] == 'lived', 'Lived_Died'] = 1
data.loc[data['Lived_Died'] == 'died', 'Lived_Died'] = 0

data['AgeRange'] = 0
data.loc[data['Age'] < 10, 'Age_Range'] = 0
data.loc[(data['Age'] >= 10) & (data['Age'] < 20), 'Age_Range'] = 10
data.loc[(data['Age'] >= 20) & (data['Age'] < 30), 'Age_Range'] = 20
data.loc[(data['Age'] >= 30) & (data['Age'] < 40), 'Age_Range'] = 30
data.loc[(data['Age'] >= 40) & (data['Age'] < 50), 'Age_Range'] = 40
data.loc[(data['Age'] >= 50) & (data['Age'] < 60), 'Age_Range'] = 50
data.loc[(data['Age'] >= 60) & (data['Age'] < 70), 'Age_Range'] = 60
data.loc[data['Age'] >= 70, 'Age_Range'] = 70

table = data.pivot_table(values='Lived_Died', index=['Gender'], columns=['Age_Range'])
print(table)
exit()

sns.set(font_scale=1.8)
xlabels = ['0-9', '10-19', '20-29', '30-39', '40-49', '50-59', '60-69', '70-$\infty$']
ax = plt.axes()
sns.heatmap(table, annot=True, yticklabels=['Male', 'Female'], xticklabels=xlabels)
ax.set_title("Heatmap Comparing Age and Gender")
plt.show()
