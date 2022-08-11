from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from yellowbrick.text import TSNEVisualizer
import os

directory = 'books'
# get only the directories in the books directory:
dirs = [d for d in os.listdir(directory) if os.path.isdir(os.path.join(directory, d))]

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

# MultinomialNB stands for multinomial Naïve Bayes
clf = MultinomialNB().fit(tfid_vect_results, labels)

books = os.listdir('test_books')
for book in books:
    print(f"For {book}, the predicted author is: ", end='')
    all_words = ''
    with open(f'test_books/{book}', 'r') as f:
        for line in f:
            all_words += line  # TfidfVectorizer expects a list of strings
    tfid_vect_results = vectorizer.transform([all_words])  # vectorizer is expecting a list
    prediction = clf.predict(tfid_vect_results)
    print(prediction[0])


    # corpus.append(all_words)

# visualize the 12 books:
# tsne = TSNEVisualizer()
# tsne.fit(tfid_vect, labels)
# tsne.show()
