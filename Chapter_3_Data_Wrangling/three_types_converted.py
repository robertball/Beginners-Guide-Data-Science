import pandas as pd

df = pd.DataFrame({'ints': [1, 2, 3, 4],
                   'strings': ['a', 'b', 'c', 'd'],
                   'floats': [1.1, '2.2', '3.3', 4]})
print(df)
print(df.dtypes)

# convert only one column:
df['floats'] = df['floats'].astype(float)

# convert all the columns based on a dictionary:
convert_dict = {'ints': int, 'strings': str, 'floats': float}
df = df.astype(convert_dict)

print('\n',df)
print(df.dtypes)

