import pandas as pd
import numpy as np
df = pd.DataFrame({'Car': [1, 1, 2, 2, 2],
                   'Type': ['new', 'used', 'new', 'used', 'used'],
                   'Price': [10, 5, 12, 7, 6]})

print(f'Original dataframe:\n{df}')

p = df.pivot_table(index='Car', columns='Type', values='Price', aggfunc=np.mean)
print(f'\nPivot table example:\n{p}')

g = df.groupby(by='Car').mean()
print(f'\nGroupby example:\n{g}')

