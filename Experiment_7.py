import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Ensure required NLTK packages are downloaded
nltk.download('punkt')
nltk.download('stopwords')

def remove_stopwords(file_path):
    # Read the passage from the text file
    try:
        with open(file_path, 'r') as file:
            text = file.read()
    except FileNotFoundError:
        print("The specified file does not exist.")
        return
    
    # Tokenize the text into words
    words = word_tokenize(text)
    
    # Get the list of stop words for English
    stop_words = set(stopwords.words('english'))
    
    # Remove stop words
    filtered_words = [word for word in words if word.lower() not in stop_words]
    
    # Join the filtered words into a cleaned passage
    cleaned_text = ' '.join(filtered_words)
    
    print("Original Passage:")
    print(text)
    print("\nCleaned Passage:")
    print(cleaned_text)

# Specify the path to the input text file
file_path = 'input.txt'  # Replace 'input.txt' with your file name
remove_stopwords(file_path)
