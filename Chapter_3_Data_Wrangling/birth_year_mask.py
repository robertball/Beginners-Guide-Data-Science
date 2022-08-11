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

# Boolean masks:
df['birth_year'] = df.birth_date.map(get_year)
boolean_mask = (df.birth_year >= 1990)
print(f'Boolean mask = \n{boolean_mask}')
print('\n', df[['first_name', 'last_name', 'birth_year']][boolean_mask])

