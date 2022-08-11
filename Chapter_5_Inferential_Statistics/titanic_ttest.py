from scipy.stats import ttest_ind
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Titanic_Passengers.csv')

df = df.drop(columns=['Name','Born','Died','Lived_Died','Fare','Passenger_Class','Age'])

df = df.dropna()

print(df)

male = df[df['Gender']=='Male']
female = df[df['Gender']=='Female']

print(male['Fare_decimal'].describe())
print(female['Fare_decimal'].describe())

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10,5))
fig.suptitle('Amount of Fare Paid Based on Gender')
ax1.boxplot(male['Fare_decimal'])
ax1.set_title('Male')
ax1.set(ylabel='Fare Amount Paid (£)')
ax1.tick_params(
    axis='x',          # changes apply to the x-axis
    which='both',      # both major and minor ticks are affected
    bottom=False,      # ticks along the bottom edge are off
    top=False,         # ticks along the top edge are off
    labelbottom=False) # labels along the bottom edge are off
ax2.boxplot(female['Fare_decimal'])
ax2.set_title('Female')
ax2.set(ylabel='Fare Amount Paid (£)')
ax2.tick_params(
    axis='x',          # changes apply to the x-axis
    which='both',      # both major and minor ticks are affected
    bottom=False,      # ticks along the bottom edge are off
    top=False,         # ticks along the top edge are off
    labelbottom=False) # labels along the bottom edge are off

#plt.show()
plt.savefig('Ball-Rague-Fig5.6.eps', bbox_inches='tight')


statistic, pvalue = ttest_ind(male['Fare_decimal'], female['Fare_decimal'])
print('\n', pvalue)
