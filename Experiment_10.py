import nltk
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

# Ensure required NLTK packages are downloaded
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')

def perform_lemmatization(sentence):
    # Initialize the WordNetLemmatizer
    lemmatizer = WordNetLemmatizer()
    
    # Tokenize the sentence into words
    words = word_tokenize(sentence)
    
    # Apply lemmatization to each word
    lemmatized_words = [lemmatizer.lemmatize(word) for word in words]
    
    # Join the lemmatized words into a sentence
    lemmatized_sentence = ' '.join(lemmatized_words)
    
    print("Original Sentence:")
    print(sentence)
    print("\nLemmatized Sentence:")
    print(lemmatized_sentence)

# Input sentence
sentence = "The leaves are falling from the trees and children are playing in the park."
perform_lemmatization(sentence)
