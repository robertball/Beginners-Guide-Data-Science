import pandas as pd
import numpy as np

# Create a dataframe:
dictionary_data = {'Column1': ['Value1', 'Value2'],  # keep adding many values as you like
        'Column2': ['Value1', 'Value2'],   # you can keep adding many columns as you like too
        }
df = pd.DataFrame(dictionary_data)

# Create another dataframe with number 0-7 in two columns:
df = pd.DataFrame(np.arange(8).reshape(4, 2), columns=['column 1', 'column 2'])

# Create a series:
data = np.array(['g', 'e', 'e', 'k', 's'])
ser = pd.Series(data)
