import pytest
from text_processing import tokenize
import sys
import os

# Add the parent directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def test_tokenize_fixed_text():
    text = 'But the Raven, sitting lonely on the placid bust, spoke only That one word...'
    expected_tokens = ['but', 'the', 'raven', 'sitting', 'lonely', 'on', 'the', 'placid', 'bust', 'spoke', 'only', 'that', 'one', 'word']
    assert tokenize(text) == expected_tokens
