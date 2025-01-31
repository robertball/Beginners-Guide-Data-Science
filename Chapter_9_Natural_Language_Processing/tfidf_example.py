from sklearn.feature_extraction.text import TfidfVectorizer

corpus = [
    'Add three eggs to the bowl. Mix the eggs with a whisk. With the bowl, add the sugar.',
    'Go to the hotel, then take get a room if there is one available. Otherwise, let\'s keep going.'
]

vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform(corpus)

print(vectorizer.get_feature_names_out())
print(X.toarray())
