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

# gets rid of nan's:
df.birth_year.dropna(inplace=True)

df['year_c3'] = pd.cut(df.birth_year, bins=3, labels=['ancient', 'middle_years', 'modern'])

c_results = df.year_c3.value_counts().sort_index()

print(c_results)

plt.title('Binning the birth years into three bins and labeling them')
plt.bar(range(len(c_results)), c_results.tolist())
plt.xticks(np.arange(len(c_results.index)), c_results.index)
plt.ylabel("Number of people born in interval")
plt.xlabel("Interval Born")

#plt.show()
plt.savefig('Ball-Rague-Fig3.7.eps', bbox_inches='tight')

