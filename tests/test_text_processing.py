import pytest
from text_processing import clean_text, tokenize, count_words


def test_clean_text():
    assert clean_text("Hello, World!") == "hello world"

def test_tokenize():
    assert tokenize("hello world") == ["hello", "world"]

def test_count_words():
    assert count_words("hello world hello") == {"hello": 2, "world": 1}
