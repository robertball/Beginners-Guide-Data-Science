from nltk.corpus import wordnet as wn

# According to the documention: There are four possible parts of speech (POS):
# verb, noun, ajective, and adverb. Synsets are identified in a 3-part form: word.pos.nn:
data = wn.synset('data.n.01')
print(f'Definition: {data.definition()}')
print(f'Examples: {data.examples()}')
print(f'Hyponyms: {data.hyponyms()}')
print(f'Member holonyms: {data.member_holonyms()}')

tab = ''
hypernym = data.hypernyms()
print(f'\nHypernyms of {data}. From {data} to {data.root_hypernyms()[0]}:')
while len(hypernym) > 0:
    print(tab, hypernym[0])
    tab += '\t'
    hypernym = hypernym[0].hypernyms()

print(f'The similarity score between {data} and {wn.synset("science.n.01")} is {data.path_similarity(wn.synset("science.n.01"))}.')
print(f'The similarity score between {data} and {wn.synset("metadata.n.01")} is {data.path_similarity(wn.synset("metadata.n.01"))}.')

