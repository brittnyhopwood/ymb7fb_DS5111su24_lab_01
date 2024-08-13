<<<<<<< HEAD
=======
[![Python CI](https://github.com/brittnyhopwood/ymb7fb_DS5111su24_lab_01/actions/workflows/validations.yml/badge.svg?event=workflow_dispatch)](https://github.com/brittnyhopwood/ymb7fb_DS5111su24_lab_01/actions/workflows/validations.yml)
# ymb7fb_DS5111su24_lab_01
Module 1 - Lab 4

## Text Processing Functions

This module provides functions for text processing, including cleaning text, tokenizing it, and counting words.

### Functions

- `clean_text(text)`: Cleans the given text by removing unwanted characters and normalizing it.
- `tokenize(text)`: Splits the cleaned text into tokens (words).
- `count_words(text)`: Counts the frequency of each word in the text.

### Example Usage

```python
from text_processing import clean_text, tokenize, count_words

text = "Sample text goes here."
cleaned = clean_text(text)
tokens = tokenize(cleaned)
word_counts = count_words(cleaned)

print("Cleaned:", cleaned)
print("Tokens:", tokens)
print("Word Counts:", word_counts)

