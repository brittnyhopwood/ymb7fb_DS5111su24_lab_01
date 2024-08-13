import sys
import pytest
import os
import requests  # Import requests
import subprocess

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from text_processing import clean_text, tokenize, count_words

# Define the paths to the text files
ENGLISH_TEXT_FILES = ["the_raven.txt"]
FRENCH_TEXT = """
Mais le Corbeau, perché solitairement sur ce buste placide, parle
ce seul mot comme si, son âme, en ce seul mot, il la répandait. Je ne
proférai donc rien de plus: il n'agita donc pas de plume--jusqu'à ce
que je fis à peine davantage que marmotter «D'autres amis déjà ont
pris leur vol--demain il me laissera comme mes Espérances déjà ont
pris leur vol.» Alors l'oiseau dit: «Jamais plus.»
"""

@pytest.mark.parametrize("filename", ENGLISH_TEXT_FILES)
def test_file_functions(filename):
    filepath = os.path.join(os.path.dirname(__file__), filename)
    
    with open(filepath, 'r') as file:
        content = file.read()
    
    # Run your tests with file content
    cleaned = clean_text(content)
    tokens = tokenize(cleaned)
    counts = count_words(content)

    # Define expected results
    expected_cleaned = clean_text(content)
    expected_tokens = tokenize(expected_cleaned)
    expected_counts = count_words(expected_cleaned)

    # Asserts
    assert cleaned == expected_cleaned
    assert tokens == expected_tokens
    assert counts == expected_counts

import requests
from text_processing import clean_text, tokenize, count_words
import pytest

@pytest.mark.integration
def test_integration_clean_tokenize_count():
    url = 'https://example.com/sample_text.txt'
    response = requests.get(url)
    text = response.text

    cleaned_text = clean_text(text)
    tokens = tokenize(cleaned_text)
    word_counts = count_words(cleaned_text)

    print(f"Cleaned text: {cleaned_text}")
    print(f"Tokens: {tokens}")
    print(f"Word counts: {word_counts}")

    common_words = ['the', 'and', 'to']
    for word in common_words:
        assert word in word_counts, f"'{word}' not found in word counts"


@pytest.mark.integration
def test_integration_clean_tokenize_count_different_file():
    url = 'https://example.com/another_sample_text.txt'
    response = requests.get(url)
    text = response.text

    cleaned_text = clean_text(text)
    tokens = tokenize(cleaned_text)
    word_counts = count_words(cleaned_text)

    print(f"Cleaned text: {cleaned_text}")
    print(f"Tokens: {tokens}")
    print(f"Word counts: {word_counts}")

    common_words = ['is', 'of', 'for']
    for word in common_words:
        assert word in word_counts, f"'{word}' not found in word counts"

@pytest.mark.skip(reason="Japanese version test not implemented yet")
def test_japanese_version():
    pass

@pytest.mark.skipif(os.name != 'nt', reason="Test only runs on Windows")
def test_windows_specific_functionality():
    pass

@pytest.mark.skipif(sys.version_info < (3, 12), reason="Test requires Python 3.12 or higher")
def test_python_version_specific_functionality():
    pass

def get_bash_output(command):
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return result.stdout.strip()

def test_bash_command_vs_function():
    test_string = "sample text"
    bash_command = f"echo {test_string}"
    bash_output = get_bash_output(bash_command)
    
    function_output = clean_text(test_string)
    
    assert bash_output.strip() == function_output, "Bash command output and function output do not match"

def test_all_english_files():
    for filename in ENGLISH_TEXT_FILES:
        filepath = os.path.join(os.path.dirname(__file__), filename)
        with open(filepath, 'r') as file:
            content = file.read()
        
        cleaned = clean_text(content)
        tokens = tokenize(cleaned)
        counts = count_words(content)

        # Define expected results
        expected_cleaned = clean_text(content)
        expected_tokens = tokenize(expected_cleaned)
        expected_counts = count_words(expected_cleaned)

        # Asserts
        assert cleaned == expected_cleaned
        assert tokens == expected_tokens
        assert counts == expected_counts

def test_french_text():
    cleaned = clean_text(FRENCH_TEXT)
    tokens = tokenize(cleaned)
    counts = count_words(FRENCH_TEXT)

    # Define expected results
    expected_cleaned = clean_text(FRENCH_TEXT)
    expected_tokens = tokenize(expected_cleaned)
    expected_counts = count_words(expected_cleaned)

    # Asserts
    assert cleaned == expected_cleaned
    assert tokens == expected_tokens
    assert counts == expected_counts
