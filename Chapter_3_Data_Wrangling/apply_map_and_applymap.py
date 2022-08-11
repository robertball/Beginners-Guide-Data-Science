import pandas as pd
import numpy as np

df = pd.DataFrame(np.arange(8).reshape(4, 2), columns=['column 1', 'column 2'])
print(f"Original dataframe:\n{df}\n")
print(f"df.apply(np.max, axis=0):\n{df.apply(np.max, axis=0)}\n")
print(f"df.apply(np.max, axis=1):\n{df.apply(np.max, axis=1)}\n")
print(f"df['column 1'].map(lambda x: x*2):\n{df['column 1'].map(lambda x: x*2)}\n")
print(f"df.applymap(lambda x: x*2):\n{df.applymap(lambda x: x*2)}")

