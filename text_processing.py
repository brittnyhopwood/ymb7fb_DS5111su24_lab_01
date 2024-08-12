import logging
import string
from collections import Counter

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def clean_text(text):
    logging.debug('Cleaning text...')
    translator = str.maketrans('', '', string.punctuation)
    cleaned_text = text.translate(translator).lower()
    return cleaned_text

def tokenize(text):
    logging.debug('Tokenizing text...')
    words = text.split()
    return words

def count_words(text):
    logging.debug('Counting words...')
    words = tokenize(clean_text(text))
    word_count = Counter(words)
    return dict(word_count)