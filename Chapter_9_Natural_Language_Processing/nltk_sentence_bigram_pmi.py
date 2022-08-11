import nltk
from nltk.collocations import *
import string

bigram_measures = nltk.collocations.BigramAssocMeasures()

text = "'I don't know', said Sally. 'I know that she went to the store. But I don't doubt that she came home right after. I don't know that it matters.'"
text = text.lower()  # this makes characters lower case

# the following removes all punctuation and changes the text into individual words:
unigrams = nltk.word_tokenize(text.translate(str.maketrans('','',string.punctuation)))
finder = BigramCollocationFinder.from_words(unigrams)
finder.apply_freq_filter(2)  # filter out all bigrams that appear less than twice
print("Most significant bigrams according to NLTK PMI:")
print(finder.nbest(bigram_measures.pmi, 10))# the ‘10’ means get the top 10 most significant collocations

