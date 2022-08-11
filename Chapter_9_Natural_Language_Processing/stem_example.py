from nltk.stem import PorterStemmer

words = ['love', 'loved', 'loves', 'loving', 'lady', 'ladies', 'strawberry', 'strawberries']
ps = PorterStemmer()

for word in words:
    print(f'{word}: {ps.stem(word)}')

