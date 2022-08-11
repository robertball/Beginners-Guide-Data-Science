from statsmodels.formula.api import ols
import matplotlib.pyplot as plt
import statsmodels.api as sm
import pandas as pd
from statsmodels.graphics.factorplots import interaction_plot

pd.set_option('display.expand_frame_repr', False)  # the ANOVA results get truncated otherwise

df = pd.read_csv('Titanic_Passengers.csv')

model = ols('Fare_decimal ~ C(Passenger_Class) + C(Gender) + C(Passenger_Class):C(Gender)', data=df).fit()
                
#actually run the anova:
aov_table = sm.stats.anova_lm(model)
print(aov_table)

fig = interaction_plot(df['Gender'], df['Passenger_Class'], df['Fare_decimal'])  #, ylabel='Mean price paid for fare (passage)')
fig.get_axes()[0].set_ylabel("Fare (£)")
plt.title('Interaction from 2-way ANOVA')

#plt.show()
plt.savefig('Ball-Rague-Fig5.8.eps', bbox_inches='tight')

