import pandas as pd
from sklearn import preprocessing

df = pd.read_csv('royal_line.csv', index_col='ID')

le = preprocessing.LabelEncoder()  # create the object

# fit (learn) and transform (create) an int representation in one step:
df['title_int'] = le.fit_transform(df['title']) 

print(df[['title', 'title_int']].head(10))

