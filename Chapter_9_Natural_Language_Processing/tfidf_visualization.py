from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from yellowbrick.text import TSNEVisualizer
import os
from sklearn.decomposition import PCA
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

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

# NOTE: TFIDF is already normalized, so it does not need to be scaled again.
pca_results = PCA(n_components=2).fit_transform(tfid_vect_results.toarray())

# print(pca_results)
color_map = {'Baum': 'red', 'Austen': 'green', 'Verne': 'blue'}
text_map = {'Baum': 'L. Frank Baum', 'Austen': 'Jane Austen', 'Verne': 'Jules Verne'}

fig, ax = plt.subplots()
i = 0
markers = {};
markers['Baum'] = 'o'
markers['Austen'] = 'P'
markers['Verne'] = '<'
for pca_result, label in zip(pca_results, labels):
    ax.scatter(pca_result[0], pca_result[1], c=color_map[label], marker=markers[label], label=text_map[label] if i % 4 == 0 else "")
    i += 1
plt.legend(frameon=True)
fig.suptitle('PCA Visualization of TFIDF data from 3 authors')
ax.grid(False)
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)
plt.style.use('plot_style.txt')
#plt.show()
plt.savefig('Ball-Rague-Fig9.1.eps', bbox_inches='tight')

