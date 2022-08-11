import pandas as pd
import numpy as np
df = pd.DataFrame(np.arange(6).reshape(3, 2), columns=['A', 'B'])
print(f'Original\n{df}')

df = df.transpose()  # or df.T

print(f'\nTransposed:\n{df}')

