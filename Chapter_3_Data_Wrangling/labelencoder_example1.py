import pandas as pd
from sklearn import preprocessing

df = pd.read_csv('royal_line.csv', index_col='ID')

le = preprocessing.LabelEncoder()  # create the object
le.fit(df['title'])  # fit or learn the data

print(le.classes_)  # not necessary, but to show the unique titles

df['title_int'] = le.transform(df['title'])  # create an int representation
print(df[['title', 'title_int']].head(10))

