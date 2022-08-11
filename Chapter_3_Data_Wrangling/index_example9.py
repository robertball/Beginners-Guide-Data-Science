import pandas as pd
import numpy as np

df = pd.DataFrame(np.arange(4).reshape(2, 2), columns=['column 1', 'column 2'], index=[1, 1])
df.reset_index(drop=True, inplace=True)
print(df)

