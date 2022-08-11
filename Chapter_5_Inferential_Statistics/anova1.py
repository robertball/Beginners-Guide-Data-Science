from statsmodels.formula.api import ols
import matplotlib.pyplot as plt
import statsmodels.api as sm
import pandas as pd

df = pd.read_csv('Titanic_Passengers.csv')

model = ols('Fare_decimal ~ C(Passenger_Class)', data=df).fit()
                
#actually run the anova:
aov_table = sm.stats.anova_lm(model)
print('ANOVA results:\n', aov_table)

df.rename(columns={'Fare_decimal': 'Fare (decimal form)', 'Passenger_Class': 'Passenger Class'}, inplace=True)  # rename so that it looks nicer for the image

df.boxplot('Fare (decimal form)', by='Passenger Class')
plt.ylabel('Fare (£)')

#plt.show()
plt.savefig('Ball-Rague-Fig5.7.eps', bbox_inches='tight')

