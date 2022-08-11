import pandas as pd
import numpy as np
df = pd.DataFrame(np.arange(12).reshape(6, 2), columns=['column 1', 'column 2'], index=['a', 'b', 'c', 'd', 'e', 'f'])
print(df)

