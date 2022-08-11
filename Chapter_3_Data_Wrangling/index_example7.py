import pandas as pd
import numpy as np

df = pd.DataFrame(np.arange(4).reshape(2, 2), columns=['column 1', 'column 2'])
print(f"First dataframe = \n{df}\nDoes it have an unique index: {df.index.is_unique}")
df = pd.DataFrame(np.arange(4).reshape(2, 2), columns=['column 1', 'column 2'], index=[1, 1])
print(f"Second dataframe = \n{df}\nDoes it have an unique index: {df.index.is_unique}")

