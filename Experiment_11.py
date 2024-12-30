import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import movie_reviews
from nltk.classify import NaiveBayesClassifier
from nltk.classify.util import accuracy
from nltk.corpus import stopwords

# Ensure required NLTK packages are downloaded
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('movie_reviews')

# Feature extraction function
def extract_features(words):
    stop_words = set(stopwords.words('english'))
    return {word: True for word in words if word.lower() not in stop_words}

# Load the movie reviews dataset
def load_dataset():
    positive_features = [(extract_features(movie_reviews.words(fileid)), 'Positive') for fileid in movie_reviews.fileids('pos')]
    negative_features = [(extract_features(movie_reviews.words(fileid)), 'Negative') for fileid in movie_reviews.fileids('neg')]
    return positive_features, negative_features

# Train the Naive Bayes Classifier
def train_classifier():
    positive_features, negative_features = load_dataset()
    train_data = positive_features[:800] + negative_features[:800]
    test_data = positive_features[800:] + negative_features[800:]
    classifier = NaiveBayesClassifier.train(train_data)
    return classifier, test_data

# Classify a given sentence
def classify_sentence(classifier, sentence):
    words = word_tokenize(sentence)
    features = extract_features(words)
    return classifier.classify(features)

# Main function
def main():
    classifier, test_data = train_classifier()
    
    # Test the classifier accuracy
    print(f"Classifier Accuracy: {accuracy(classifier, test_data) * 100:.2f}%")
    
    # Classify a sample sentence
    sample_sentence = "The plot was dull and the acting was terrible."
    classification = classify_sentence(classifier, sample_sentence)
    print(f"Input Sentence: \"{sample_sentence}\"")
    print(f"Classification: {classification}")
    
    # Show top features
    print("\nMost Informative Features:")
    classifier.show_most_informative_features(10)

if __name__ == "__main__":
    main()
