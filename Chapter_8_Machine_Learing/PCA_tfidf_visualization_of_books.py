from sklearn.feature_extraction.text import TfidfVectorizer
import os
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

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

color_map = {'howells': 'red', 'huxley': 'green', 'jacobs': 'blue', 'potter': 'yellow', 'thornton': 'purple',
             'trollope': 'black'}

fig, ax = plt.subplots()
i = 0
j = 0
markers = ['o','v','s','p','P','H']
temp_label = labels[0]
author = labels[0]
for pca_result, label in zip(pca_results, labels):
    ax.scatter(pca_result[0], pca_result[1], marker=markers[j], c=color_map[label], label=label if i == 0 else "")
    i = 1 if author == label else 0
    author = label
    if temp_label != label:
        j += 1
        temp_label = label

plt.legend(frameon=True)
fig.suptitle('PCA Visualization of TFIDF data for 344 books')
ax.grid(False)
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)
#plt.show()
plt.style.use('plot_style.txt')
plt.savefig('Ball-Rague-Fig8.29.eps', bbox_inches='tight')

