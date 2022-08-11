import pandas as pd
import numpy as np
df = pd.DataFrame(np.arange(12).reshape(6, 2), columns=['column 1', 'column 2'], index=[4, 2, 1, 3, 5, 0])
print(df)

