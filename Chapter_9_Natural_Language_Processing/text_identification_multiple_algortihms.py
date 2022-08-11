from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.datasets import fetch_20newsgroups
from sklearn.pipeline import Pipeline
import numpy as np
from sklearn.linear_model import SGDClassifier
from sklearn.svm import LinearSVC
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics

categories = ['alt.atheism', 'soc.religion.christian', 'comp.graphics', 'sci.med']

twenty_train = fetch_20newsgroups(subset='train', categories=categories, shuffle=True, random_state=13)  # gets test text for us

# The returned dataset is a scikit-learn “bunch”: a simple holder object with fields
# that can be both accessed as python dict keys or object attributes for convenience, for instance the
# target_names holds the list of the requested category names:
print(twenty_train.target_names)

print(len(twenty_train.data))

print(len(twenty_train.filenames))

# Let’s print the first lines of the first loaded file:
print("\nFirst line of the first loaded file:")
print("\n".join(twenty_train.data[0].split("\n")[:3]))
print("\nThe category:")
print(twenty_train.target_names[twenty_train.target[0]])

# For speed and space efficiency reasons scikit-learn loads the target
# attribute as an array of integers that corresponds to the index of the
# category name in the target_names list. The category
# integer id of each sample is stored in the target attribute:
print("\n\nexample categories in dataset:")
print(twenty_train.target[:10])

print("\nOr, if we use those values as indices:")
for t in twenty_train.target[:10]:
    print(twenty_train.target_names[t])

# In order to perform machine learning on text documents, we first need to turn the text content into numerical feature vectors:

# Bags of Words:
# The most intuitive way to do so is the bags of words representation:

#        assign a fixed integer id to each word occurring in any document of the training set (for instance by building a dictionary from words to integer indices).
#        for each document #i, count the number of occurrences of each word w and store it in X[i, j] as the value of feature #j where j is the index of word w in the dictionary

# The bags of words representation implies that n_features is the number of distinct words in the corpus: this number is typically larger than 100,000.

# If n_samples == 10000, storing X as a numpy array of type float32 would require 10000 x 100000 x 4 bytes = 4GB in RAM which is barely manageable on today’s computers.

# Fortunately, most values in X will be zeros since for a given document less than a couple thousands of distinct words will be used. For this reason we say that bags of words are typically high-dimensional sparse datasets. We can save a lot of memory by only storing the non-zero parts of the feature vectors in memory.

# scipy.sparse matrices are data structures that do exactly this, and scikit-learn has built-in support for these structures.

# Text preprocessing, tokenizing and filtering of stopwords are included in a high level component that is able to build a dictionary of features and transform documents to feature vectors:
count_vect = CountVectorizer()
X_train_counts = count_vect.fit_transform(twenty_train.data)
print("\nThe size of the count vector:")
print(X_train_counts.shape)

print("\nCountVectorizer supports counts of N-grams of words or consecutive characters. Once fitted, the vectorizer has built a dictionary of feature indices:")
print("For example, how often does 'algorithm' show up?")
print(count_vect.vocabulary_.get(u'algorithm'))

# From occurrences to frequencies:
# Occurrence count is a good start but there is an issue: longer documents will
# have higher average count values than shorter documents, even though they might
# talk about the same topics.

# To avoid these potential discrepancies it suffices to divide the number of
# occurrences of each word in a document by the total number of words in the
# document: these new features are called tf for Term Frequencies.

# Another refinement on top of tf is to downscale weights for words that occur
# in many documents in the corpus and are therefore less informative than those
# that occur only in a smaller portion of the corpus.

# This downscaling is called tf–idf for “Term Frequency times Inverse Document Frequency”.

# Both tf and tf–idf can be computed as follows:

tfidf_transformer = TfidfTransformer()
X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)
print("The shape of 'X_train_tfidf':")
print(X_train_tfidf.shape)

# Now that we have our features, we can train a classifier to try to
# predict the category of a post. Let’s start with a naïve Bayes classifier,
# which provides a nice baseline for this task. scikit-learn includes several
# variants of this classifier; the one most suitable for word counts is the multinomial variant:
clf = MultinomialNB().fit(X_train_tfidf, twenty_train.target)

# To try to predict the outcome on a new document we need to extract
# the features using almost the same feature extracting chain as before.
# The difference is that we call transform instead of fit_transform on the
# transformers, since they have already been fit to the training set:
docs_new = ['God is love', 'OpenGL on the GPU is fast']
X_new_counts = count_vect.transform(docs_new)
X_new_tfidf = tfidf_transformer.transform(X_new_counts)

predicted = clf.predict(X_new_tfidf)

for doc, category in zip(docs_new, predicted):
    print('%r => %s' % (doc, twenty_train.target_names[category]))

print("\n")
# n order to make the vectorizer => transformer => classifier easier
# to work with, scikit-learn provides a Pipeline class that behaves
# like a compound classifier:
text_clf = Pipeline([('vect', CountVectorizer()),
                     ('tfidf', TfidfTransformer()),
                     ('mnb', MultinomialNB())
                     ])

# The names vect, tfidf and clf (classifier) are arbitrary.
# We shall see their use in the section on grid search, below.
# We can now train the model with a single command:
text_clf.fit(twenty_train.data, twenty_train.target)

# Now we evaluate the predictive accuracy of the model:
twenty_test = fetch_20newsgroups(subset='test', categories=categories, shuffle=True, random_state=42)

docs_test = twenty_test.data

predicted = text_clf.predict(docs_test)
print("The average correct for the Multinomial Naive Bayes:")
print(np.mean(predicted == twenty_test.target), '\n')

text_clf = Pipeline([('vect', CountVectorizer()),
                     ('tfidf', TfidfTransformer()),
                     ('svm', SGDClassifier(loss='hinge', penalty='l2',
                                           alpha=1e-3, random_state=42,
                                           max_iter=50, tol=1e-3))
                     ])
text_clf.fit(twenty_train.data, twenty_train.target)
predicted = text_clf.predict(docs_test)
print("The average correct for the Stochastic Gradient Descend (SGD) with linear SVM (Support Vector Machine)")
print(np.mean(predicted == twenty_test.target), '\n')

text_clf = Pipeline([('vect', CountVectorizer()),
                     ('tfidf', TfidfTransformer()),
                     ('lr', LinearSVC())
                     ])
text_clf.fit(twenty_train.data, twenty_train.target)
predicted = text_clf.predict(docs_test)
print("The average correct for the plain Support Vector Machine (SVM):")
print(np.mean(predicted == twenty_test.target), '\n')

text_clf = Pipeline([('vect', CountVectorizer()),
                     ('tfidf', TfidfTransformer()),
                     ('rf', RandomForestClassifier(n_estimators=200, max_depth=3, random_state=0))
                     ])
text_clf.fit(twenty_train.data, twenty_train.target)
predicted = text_clf.predict(docs_test)
print("The average correct for the Random Forest Classifier:")
print(np.mean(predicted == twenty_test.target), '\n')

text_clf = Pipeline([('vect', CountVectorizer()),
                     ('tfidf', TfidfTransformer()),
                     ('lr', LogisticRegression(random_state=0, solver="lbfgs", multi_class="auto"))
                     ])
text_clf.fit(twenty_train.data, twenty_train.target)

predicted = text_clf.predict(docs_test)
print("The average correct for the Logistic Regression:")
print(np.mean(predicted == twenty_test.target))
