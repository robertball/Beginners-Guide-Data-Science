import pandas as pd
import numpy as np
df = pd.DataFrame({'Car': [1, 1, 2, 2, 2],
                   'Type': ['new', 'used', 'new', 'used', 'used'],
                   'Price': [10, 5, 12, 7, 6]})

print(df.groupby(by=['Car', 'Type']).agg(['mean', 'sum']))

