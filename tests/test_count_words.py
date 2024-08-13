import pytest
from text_processing import count_words
import sys
import os

# Add the parent directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def test_count_words_fixed_text():
    text = 'But the Raven, sitting lonely on the placid bust, spoke only That one word...'
    expected_count = {'but': 1, 'the': 2, 'raven': 1, 'sitting': 1, 'lonely': 1, 'on': 1, 'placid': 1, 'bust': 1, 'spoke': 1, 'only': 1, 'that': 1, 'one': 1, 'word': 1}
    assert count_words(text) == expected_count
