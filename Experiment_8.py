import nltk
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

# Ensure required NLTK packages are downloaded
nltk.download('punkt')

def perform_stemming(sentence):
    # Initialize the PorterStemmer
    stemmer = PorterStemmer()
    
    # Tokenize the sentence into words
    words = word_tokenize(sentence)
    
    # Apply stemming to each word
    stemmed_words = [stemmer.stem(word) for word in words]
    
    # Join the stemmed words into a sentence
    stemmed_sentence = ' '.join(stemmed_words)
    
    print("Original Sentence:")
    print(sentence)
    print("\nStemmed Sentence:")
    print(stemmed_sentence)

# Input sentence
sentence = "The cats are running faster than the dogs, and they will be jumping again soon."
perform_stemming(sentence)
