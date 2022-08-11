from nltk.corpus import stopwords

# the following two lines need to only be run once:
import nltk
nltk.download('stopwords')  # needs to be run only only!

stop_words = stopwords.words('english')
print(stop_words)

