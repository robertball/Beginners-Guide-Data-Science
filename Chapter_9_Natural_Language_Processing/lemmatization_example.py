from nltk.stem import WordNetLemmatizer
# import nltk
# nltk.download('wordnet')  # this only has to be done once!
  
lemmatizer = WordNetLemmatizer()

words = ['love', 'loved', 'loves', 'loving', 'lady', 'ladies', 'strawberry', 'strawberries']

for word in words:
    print(f'{word}:\t noun: {lemmatizer.lemmatize(word)}\t adjective: {lemmatizer.lemmatize(word, pos="a")}\t verb: {lemmatizer.lemmatize(word, pos="v")}')
  
