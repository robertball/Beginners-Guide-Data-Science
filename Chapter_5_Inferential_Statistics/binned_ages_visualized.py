import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

bin_list = [0, 10, 20, 30, 40, 50, 60, 70, 80]

df = pd.read_csv('Titanic_Passengers.csv')

df.dropna(subset=['Age'], inplace=True)

female_ages = pd.cut(x=df[df['Gender'] == 'Female']['Age'], bins=bin_list)
male_ages = pd.cut(x=df[df['Gender'] == 'Male']['Age'], bins=bin_list)

male_values = [value for value in male_ages.value_counts(sort=False)]
female_values = [value for value in female_ages.value_counts(sort=False)]

survived = pd.cut(x=df[df['Lived_Died'] == 'lived']['Age'], bins=bin_list)
died = pd.cut(x=df[df['Lived_Died'] == 'died']['Age'], bins=bin_list)

x = np.arange(len(male_values))  # the label locations
width = 0.35  # the width of the bars

labels = [str(label) for label in died.unique()]
survived_values = [value for value in survived.value_counts(sort=False)]
died_values = [value for value in died.value_counts(sort=False)]

fig, ax = plt.subplots(figsize=(10,5))
ax.bar(x - width / 2, survived_values, width, label='Survived')
ax.bar(x + width / 2, died_values, width, label='Died')
plt.ylabel('Count')
plt.xlabel('Age Ranges')
plt.title('Histogram of Age Ranges of Titantic Passengers')
plt.legend()
ax.set_xticks(range(len(labels)))
ax.set_xticklabels(labels)

#plt.show()
plt.savefig('Ball-Rague-Fig5.2.eps', bbox_inches='tight')

