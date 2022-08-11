import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def get_year(x):
    if pd.isna(x):
        year_result = np.nan  # if the birth_year is nan then return nan
    else:  # checking a number of edge cases in the data and stripping it out:
        if "ABT" in x:  # for example: ABT  1775  
            x = x[3:]
            x = x.strip()
        if "/" in x:  #  For example: 1775/1776
            x = x[:x.find('/')]
        num_spaces = x.count(' ')
        if num_spaces == 0:  # only has the year
            year_result = int(x)
        elif num_spaces == 1:  # example: FEB 1337
            x = x[x.rfind(' ') + 1:]  # 'rfind' finds the last space. The 'r' stands for 'reverse.'
            if x.isnumeric():
                year_result = int(x)
            else:  # This could happen if there is only a day and month, like '10 JAN'
                year_result = np.nan
        elif num_spaces == 2:  # example: 16 FEB 1337
            x = x[x.rfind(' ') + 1:]  # 'rfind' finds the last space. The 'r' stands for 'reverse.'
            year_result = int(x)
        else:
            year_result = np.nan  # There are a few other strange dates that aren't worth our time to fix, so just return nan for those.
    return year_result

df = pd.read_csv('royal_line.csv', index_col='ID')
df['birth_year'] = df['birth_date'].map(get_year)

# gets rid of nan's and return a list:
just_birth_years = df.birth_year.dropna().tolist()  
just_birth_years = sorted(just_birth_years)  # sort the birth years
years_count = {}  # create a dictionary of year to number of births
for year in np.arange(just_birth_years[0], just_birth_years[-1]): 
    years_count[year] = 0  # set a default of zero births to every year

for year in just_birth_years:
    if year in years_count:
        years_count[year] += 1  # add 1 for every birth year found in the data 
    
plt.figure(figsize=(10,5))
plt.bar(range(len(years_count)), list(years_count.values()))  # bar chart
plt.xticks([])  # remove the year labels - there are too many to show
plt.ylabel('Number of people born in year')
plt.xlabel('Year Born')
plt.title('Histogram of birth years')

#plt.show()
plt.savefig('Ball-Rague-Fig3.4.eps', bbox_inches='tight')
