import pandas as pd
import numpy as np

df = pd.DataFrame(np.arange(12).reshape(6, 2), columns=['column 1', 'column 2'])
print(df)

new_df = df.apply(lambda column: column.max())
print(f'\nThe result =\n{new_df}')

