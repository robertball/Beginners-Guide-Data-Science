import nltk
import string
import math


def bigram_pmi(bigram_tuple, unigram_frequency, bigram_frequency):
    pw1 = unigram_frequency[bigram_tuple[0]] / float(sum(unigram_frequency.values()))
    pw2 = unigram_frequency[bigram_tuple[1]] / float(sum(unigram_frequency.values()))
    p_w1_w2 = bigram_frequency[bigram_tuple] / float(sum(bigram_frequency.values()))
    return math.log(p_w1_w2 / float(pw1 * pw2), 2)


input_text = "'I don't know', said Sally. 'I know that she went to the store. But I don't doubt that she came home right after. I don't know that it matters.'"
input_text = input_text.lower()  # this makes characters lower case
sentences = nltk.sent_tokenize(input_text)  # change the text into individual sentences

translator = str.maketrans('', '', string.punctuation)  # make translator object to remove punctuation

sentences = [sentence.translate(translator) for sentence in sentences]  # remove punctuation from each sentence
# it is important to tokenize into sentences before taking out punctuation or else how can you tell one sentence from another?

tokenized_sentences = list(map(nltk.tokenize.word_tokenize, sentences))  # separates the txt into a list of words for each sentence

bigrams = []
for sentence in tokenized_sentences:  # get bigrams for each sentence
    bigrams.extend(list(nltk.ngrams(sentence, 2)))

# this gets the frequency of every bigram:
bigrams_frequency = {}
for b in bigrams:
    print(b)
    if b not in bigrams_frequency:
        bigrams_frequency[b] = 1
    else:
        bigrams_frequency[b] += 1

filtered_bigrams = []
# remove any bigram's whose frequency is less than 2:
for key in bigrams_frequency:
    print(f"key = {key}: {bigrams_frequency[key]}")
    if bigrams_frequency[key] >= 2:
        filtered_bigrams.append(key)

print(filtered_bigrams)

unigrams = nltk.word_tokenize(input_text.translate(translator))
print("\nunigrams:")
print(unigrams)

# this gets the frequency of every unigram:
unigrams_frequency = {}
for u in unigrams:
    if u not in unigrams_frequency:
        unigrams_frequency[u] = 1
    else:
        unigrams_frequency[u] += 1

bigram_scores = {}
for b in filtered_bigrams:
    print(b)
    bigram_scores[b] = bigram_pmi(b, unigram_frequency=unigrams_frequency, bigram_frequency=bigrams_frequency)

results = sorted(bigram_scores, key=bigram_scores.get, reverse=True)  # sort the results based on the score

print("Most significant bigrams according to PMI:")
print(results)
