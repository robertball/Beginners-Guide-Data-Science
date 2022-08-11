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

df['year_q4'] = pd.qcut(df.birth_year, q=4)
df['year_c4'] = pd.cut(df.birth_year, bins=4)
q_results = df.year_q4.value_counts().sort_index()
c_results = df.year_c4.value_counts().sort_index()

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10,5))  # create two plots: 1 row, 2 columns
fig.suptitle('qcut example (left) with cut example (right) with 4 bins each')

ax1.bar(range(len(q_results)), q_results.tolist())  # bar chart
ax1.set_xticks(np.arange(len(q_results.index)))  # set the # of xticks
ax1.set_xticklabels(q_results.index)  # set the values of the xticks
ax1.set_xlabel('Interval Born')
ax1.set_ylabel("Number of people born in interval")

ax2.bar(range(len(c_results)), c_results.tolist())  # bar chart
ax2.set_xticks(np.arange(len(c_results.index)))  # set the # of xticks
ax2.set_xticklabels(c_results.index)  # set the values of the xticks
ax2.set_xlabel('Interval Born')

ax1.tick_params(axis='both', which='major', labelsize=6)
ax2.tick_params(axis='both', which='major', labelsize=6)

#plt.show()
plt.savefig('Ball-Rague-Fig3.5.eps', bbox_inches='tight')

