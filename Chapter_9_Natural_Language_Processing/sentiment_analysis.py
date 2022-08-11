from nltk.sentiment.vader import SentimentIntensityAnalyzer
#import nltk
#nltk.download('vader_lexicon')  # this only has to be done once!)

corpus = [
        "I love to eat delicious pie on Sundays!",
        "My father died and I am horribly depressed.",
        "Watermelon grows on vines."
]

analyzer = SentimentIntensityAnalyzer()

for sentence in corpus:
    print(f'The sentence: {sentence}\nThe score: {analyzer.polarity_scores(sentence)}\n')
