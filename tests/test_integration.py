# tests/test_integration.py
import pytest
from text_processing import clean_text, tokenize, count_words
import requests

@pytest.mark.integration
def test_integration_clean_tokenize_count():
    url = 'https://example.com/sample_text.txt'
    response = requests.get(url)
    text = response.text
    
    cleaned_text = clean_text(text)
    tokens = tokenize(cleaned_text)
    word_counts = count_words(cleaned_text)
    
    common_words = ['the', 'and', 'to']
    for word in common_words:
        assert word in word_counts
        assert word_counts[word] > 0

@pytest.mark.integration
def test_integration_clean_tokenize_count_different_file():
    url = 'https://example.com/another_sample_text.txt'
    response = requests.get(url)
    text = response.text
    
    cleaned_text = clean_text(text)
    tokens = tokenize(cleaned_text)
    word_counts = count_words(cleaned_text)
    
    common_words = ['is', 'of', 'for']
    for word in common_words:
        assert word in word_counts
        assert word_counts[word] > 0
