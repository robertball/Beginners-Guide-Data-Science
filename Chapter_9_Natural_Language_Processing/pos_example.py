import nltk
#nltk.download('punkt')  # this only has to be done once!
#nltk.download('averaged_perceptron_tagger')  # this only has to be done once!

text = "I like to eat yummy strawberries on Sundays!"
tokens = nltk.word_tokenize(text)
print(tokens)
tag = nltk.pos_tag(tokens)
print(tag)

