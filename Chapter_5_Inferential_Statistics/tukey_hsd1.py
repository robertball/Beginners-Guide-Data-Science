import statsmodels.api as sm
from statsmodels.formula.api import ols
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
from statsmodels.stats.multicomp import pairwise_tukeyhsd
from statsmodels.stats.multicomp import MultiComparison
import seaborn as sns
import numpy as np
from scipy import stats

df = pd.read_csv('Titanic_Passengers.csv')

df.drop(columns=['Born', 'Died', 'Age', 'Fare', 'Lived_Died', 'Name', 'Gender'], inplace=True)  # get rid of the unnecessary columns. This is needed so that we don't get rid of rows tha we can keep in the next line that drops the NA's.
df.dropna(inplace=True)  # drop all the NA's - the empty rows. If you do not drop the NA's then it will not work!!

mc = MultiComparison(df['Fare_decimal'], df['Passenger_Class'])
result = mc.tukeyhsd()
print(result)

