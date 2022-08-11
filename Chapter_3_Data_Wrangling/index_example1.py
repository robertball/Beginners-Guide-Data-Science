import pandas as pd
import numpy as np

df = pd.DataFrame(np.arange(10).reshape(5, 2), columns=['A', 'B'], index=['cat', 42, 'stone', 42, 12345])# Five rows each with an associated index
print(df)

