
import nltk
from nltk.stem import PorterStemmer

nltk.download('punkt')

# Create a PorterStemmer object
stemmer = PorterStemmer()

# List of words to stem
words = ["running", "jumping", "happiness", "computers", "generous"]

# Perform word stemming
stemmed_words = [stemmer.stem(word) for word in words]

print(stemmed_words)
