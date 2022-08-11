from sklearn.feature_extraction.text import CountVectorizer

corpus = [
    'Add three eggs to the bowl. Mix the eggs with a whisk. With the bowl, add the sugar.',
    'Go to the hotel, then take get a room if there is one available. Otherwise, let\'s keep going.'
]

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(corpus)

print(vectorizer.get_feature_names())
print(X.toarray())

