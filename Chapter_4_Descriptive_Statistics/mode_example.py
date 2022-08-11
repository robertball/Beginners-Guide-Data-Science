import pandas as pd
iris_df = pd.read_csv('iris.csv')
print(f'mode of the Iris sepal length is \n{iris_df["sepal_length"].mode()}')

mode_df = pd.DataFrame([1, 2, 3], columns=['a'])
print(f'\nmode of [1, 2, 3] is \n{mode_df["a"].mode()}')

mode_df = pd.DataFrame([1, 2, 2, 3], columns=['a'])
print(f'\nmode of [1, 2, 2, 3] is \n{mode_df["a"].mode()}')

mode_df = pd.DataFrame([1, 2, 2, 3, 3, 5], columns=['a'])
print(f'\nmode of [1, 2, 2, 3, 3, 5] is \n{mode_df["a"].mode()}')
