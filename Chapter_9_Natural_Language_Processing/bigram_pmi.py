def bigram_pmi(bigram_tuple, unigram_frequency, bigram_frequency):
    pw1 = unigram_frequency[bigram_tuple[0]]/float(sum(unigram_frequency.values()))
    pw2 = unigram_frequency[bigram_tuple[1]]/float(sum(unigram_frequency.values()))
    p_w1_w2 = bigram_frequency[bigram_tuple]/float(sum(bigram_frequency.values()))
    return math.log(p_w1_w2/float(pw1*pw2),2)

