"""
This module provides functions for text processing tasks, including
cleaning text, tokenizing it, and counting words.

Functions:
- clean_text: Cleans the input text.
- tokenize: Tokenizes the input text into words.
- count_words: Counts the occurrences of each word in the text.
"""

import logging
import string
from collections import Counter

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def clean_text(text):
    """
    Cleans the input text by removing unwanted characters and whitespace.

    Args:
        text (str): The text to be cleaned.

    Returns:
        str: The cleaned text.
    """
    # Function implementation
    logging.debug('Cleaning text...')
    translator = str.maketrans('', '', string.punctuation)
    cleaned_text = text.translate(translator).lower()
    return cleaned_text

def tokenize(text):
    """
    Tokenizes the input text into individual words.

    Args:
        text (str): The text to be tokenized.

    Returns:
        list: A list of words from the text.
    """
    logging.debug('Tokenizing text...')
    text = clean_text(text)  # Ensure text is cleaned before tokenizing
    words = text.split()
    return words


def count_words(text):
    """
    Counts the occurrences of each word in the input text.

    Args:
        text (str): The text to be analyzed.

    Returns:
        dict: A dictionary where keys are words and values are their counts.
    """
    logging.debug('Counting words...')
    words = tokenize(clean_text(text))
    word_count = Counter(words)
    return dict(word_count)

