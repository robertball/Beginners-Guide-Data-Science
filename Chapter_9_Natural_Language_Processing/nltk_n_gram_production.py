import nltk
import string
text = "This is example text. Getting collocations from a small amount of text is not very valuable. Collocations are usually performed on thousands to millions of words."
# this next step removes all punctuation from the text and 
# makes all the text lowercase:
text = text.translate(str.maketrans('','',string.punctuation)).lower() 
# this next step breaks the string into individual words:
text2 = nltk.word_tokenize(text)
for i in range(2, 6): # for loop that generates all 2-grams to 5-grams
        print(f"{i}-grams: \n{list(nltk.ngrams(text2, i))}") 

