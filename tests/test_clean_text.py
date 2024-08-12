import pytest
from ..text_processing import clean_text  # Import from text_processing.py
import sys
import os

# Add the parent directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def test_clean_text_fixed_text():
    text = 'But the Raven, sitting lonely on the placid bust, spoke only That one word...'
    expected_cleaned_text = 'but the raven sitting lonely on the placid bust spoke only that one word'
    assert clean_text(text) == expected_cleaned_text
