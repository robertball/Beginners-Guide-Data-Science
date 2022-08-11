import pandas as pd

iris_df = pd.read_csv('iris.csv')

print(iris_df['sepal_length'].mean())

