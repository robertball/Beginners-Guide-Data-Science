import pandas as pd

df = pd.DataFrame({'ints': [1, 2, 3, 4],
                   'strings': ['a', 'b', 'c', 'd'],
                   'floats': [1.1, '2.2', '3.3', 4]})
print(df)
print(df.dtypes)

