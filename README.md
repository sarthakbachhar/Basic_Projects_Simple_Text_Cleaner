# Text Cleaner with Stemming and Lemmatization

This project demonstrates basic text preprocessing by removing punctuation, stopwords, and applying both stemming and lemmatization.

## Requirements

- Python 3.x
- NLTK
- SpaCy

## Setup

1. Install the required libraries:

   ```bash
   pip install nltk spacy
   python -m spacy download en_core_web_sm

2. Download the NLTK stopwords:

   ```bash
   import nltk
   nltk.download('stopwords')

## Usage

* Stemming: Uses NLTK's PorterStemmer to stem words after removing punctuation and stopwords.
* Lemmatization: Uses SpaCy to lemmatize words and includes a custom rule for specific words (e.g., "Bro" -> "Brother").
  
## Running the Script

1. Prepare the text data.
2. Run the script to clean the text and display stemmed and lemmatized words.
   
## Example
The script processes a text, removing stopwords, punctuation, and applying both stemming and lemmatization, with results printed to the console.

## License
MIT License. Feel free to use and modify.
