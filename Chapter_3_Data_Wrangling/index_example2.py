import pandas as pd
import numpy as np

df = pd.DataFrame(np.arange(10).reshape(5, 2), columns=['A', 'B'], index=['cat', 42, 'stone', 42, 12345])# Five rows each with an associated index

print(df.loc[12345])  # prints the last row: values 8 & 9
print(df.loc['stone'])  # prints the third row: values 4 & 5
print(df.loc[42])  # prints two rows (because two rows have the label 42)
print(df.loc['A'])  # produces an error. There is no row labeled 'A'
print(df.loc['cat':'stone'])  # prints the first three rows
print(df.loc[['cat', 'stone']])  # prints the first and third rows
print(df.loc['stone', 'B'])  # prints the value of 5: row 'stone', column 'B'
print(df.loc[df['A'] > 3])  # prints the last three rows

# using conditionals:
# row 12345, column 'A' == 8, so it changes the value in column 'B' to 120:
df.loc[df['A'] == 8, 'B'] = 120
print(df.loc[12345])  # prints 8 & 120, showing the change

print(df.iloc[0])  # print the first row with the values of 0 & 1
print(df.iloc[0:3])  # print the first three rows
print(df.iloc[[0, 2, 4]])  # prints 'cat,' 'stone,' and 1234 rows
print(df.iloc[0, 1])  # prints the first (zeroeth) row ('cat') for column 'B'
print(df.iloc[0:3, 1])  # prints the first 3 rows for column 'B'

