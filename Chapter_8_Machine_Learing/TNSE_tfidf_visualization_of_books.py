import os
from yellowbrick.text import TSNEVisualizer
from sklearn.feature_extraction.text import TfidfVectorizer

folders = os.listdir()
dir = 'books'
dirs = [d for d in os.listdir(dir) if os.path.isdir(os.path.join(dir, d))]

corpus = []
labels = []
for directory in dirs:
    books = os.listdir(f'books/{directory}')
    for book in books:
        labels.append(directory)
        all_words = ''
        with open(f'books/{directory}/{book}', 'r') as f:
            for line in f:
                all_words += line  # TfidfVectorizer expects a list of strings
        corpus.append(all_words)

vectorizer = TfidfVectorizer(stop_words='english')
tfid_vect_results = vectorizer.fit_transform(corpus)

markers = ['o','v','s','p','P','H']

#tsne = TSNEVisualizer(markers=markers)
tsne.fit(tfid_vect_results, labels)
tsne.show()
