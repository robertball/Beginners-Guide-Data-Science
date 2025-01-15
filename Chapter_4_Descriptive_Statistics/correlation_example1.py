import pandas as pd
df = pd.read_csv('iris.csv')
correlation = df['petal_length'].corr(df['petal_width']) #Spearman, Pearson, or Kendall can be specified. Pearson is the default.
print(f'The resulting R-value of petal length to petal width: {correlation}.')

