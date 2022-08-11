def add_collocation(collocation, collocation_length, results):
    if collocation_length not in results:
        results[collocation_length] = dict()
    if collocation not in results[collocation_length]:
        results[collocation_length][collocation] = 1
    else:
        results[collocation_length][collocation] += 1

def get_collocations(text):
    results = dict()
    words = text.split()
    if len(words) == 0:
        return
    for i in range(1, len(words)):
        beg = 0
        end = beg + i
        while end <= len(words):
            collocation = " ".join(words[beg:end])
            add_collocation(collocation, i, results)
            beg += 1
            end += 1
    return results

example_text = 'The watermelon is considered ripe when the vine that it connect to starts to wither.'
print(f'Original text:\n{example_text}')
collocations = get_collocations(example_text)

for key in collocations.keys():
    print(f'{key}-grams: {collocations[key]}')

