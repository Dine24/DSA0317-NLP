import nltk
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
def perform_morphological_analysis(text):
    words = word_tokenize(text)
    print(words)
    porter_stemmer = PorterStemmer()
    print(porter_stemmer)
    stemmed_words = [porter_stemmer.stem(word) for word in words]
    return stemmed_words
input_text = "Plants are living beings, if im not wrong"
result = perform_morphological_analysis(input_text)
print("Original Text:")
print(input_text)
print("\nMorphological Analysis:")
print(result)
