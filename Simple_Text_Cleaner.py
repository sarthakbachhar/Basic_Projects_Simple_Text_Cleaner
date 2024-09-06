import nltk
import spacy
import string

# For stemming
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

# Initialize stemmer and stopwords
stemmer = PorterStemmer()
stop_words = set(stopwords.words('english'))

# Sample text for stemming 
words = "The quick brown foxes are jumping over the lazy dogs. The runners were running rapidly because they had to run faster than before. Eating apples and oranges is a healthy habit. She enjoys the hiking and the various hiking trails."

# Stemming without stopwords or punctuation
tokens = word_tokenize(words.lower())
for token in tokens:
  if token not in string.punctuation and token not in stop_words:
    print(token, "=", stemmer.stem(token), "|", end=" ")
print("\n")

# Initialize spacy model for Lemmatization
nlp = spacy.load("en_core_web_sm")

# Adding custom word rules
ar = nlp.get_pipe('attribute_ruler')
ar.add([[{"TEXT":"Bro"}], [{"TEXT": "Brah"}]], {"LEMMA":"Brother"})

# Text for Lemmatization
text = "The quick brown foxes are jumping over the lazy dogs. The runners were running rapidly because they had to run faster than before. Eating apples and oranges is a healthy habit. She enjoys the hiking and the various hiking trails."

# Process the text with spacy
doc = nlp(text)

for token in doc:
  # Remove punctuation and stop words
  if token.text not in string.punctuation and not token.is_stop:
    print(token, "=", token.lemma_, "|", end=" ")
