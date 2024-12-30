import nltk

# Ensure required NLTK packages are downloaded
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

def pos_tagging(sentence):
    # Tokenize the sentence into words
    words = nltk.word_tokenize(sentence)
    
    # Perform POS tagging
    pos_tags = nltk.pos_tag(words)
    
    print("Parts of Speech Tags:")
    for word, tag in pos_tags:
        print(f"{word} -> {tag}")

# Input sentence
sentence = "The quick brown fox jumps over the lazy dog."
pos_tagging(sentence)
