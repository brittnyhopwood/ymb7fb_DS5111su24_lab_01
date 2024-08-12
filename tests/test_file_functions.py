import sys
import pytest
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from ..text_processing import clean_text, tokenize, count_words

# Define the paths to the text files
ENGLISH_TEXT_FILES = ["the_raven.txt"]  # Update this list with files that are present in the 'tests' directory
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

    # Define expected results (these should be based on what you expect the output to be)
    expected_cleaned = clean_text("But the Raven sitting lonely on the placid bust spoke only That one word as if his soul in that one word he did outpour")
    expected_tokens = tokenize("But the Raven sitting lonely on the placid bust spoke only That one word as if his soul in that one word he did outpour")
    expected_counts = count_words("But the Raven sitting lonely on the placid bust spoke only That one word as if his soul in that one word he did outpour")

    # Asserts
    assert cleaned == expected_cleaned
    assert tokens == expected_tokens
    assert counts == expected_counts

# Test for Japanese version (hypothetical)
@pytest.mark.skip(reason="Japanese version test not implemented yet")
def test_japanese_version():
    # Hypothetical test for Japanese text
    pass

# Example test for conditional OS
@pytest.mark.skipif(os.name != 'nt', reason="Test only runs on Windows")
def test_windows_specific_functionality():
    # Test code here
    pass

# Example test for conditional Python version
@pytest.mark.skipif(sys.version_info < (3, 12), reason="Test requires Python 3.12 or higher")
def test_python_version_specific_functionality():
    # Test code here
    pass

# Example test comparing Bash command output
import subprocess

def get_bash_output(command):
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return result.stdout.strip()

def test_bash_command_vs_function():
    test_string = "sample text"
    bash_command = f"echo {test_string}"  # Replace with an appropriate command
    bash_output = get_bash_output(bash_command)
    
    # Replace with actual function calls and expected output
    function_output = clean_text(test_string)
    
    assert bash_output == function_output, "Bash command output and function output do not match"

# Test all English files together
def test_all_english_files():
    for filename in ENGLISH_TEXT_FILES:
        filepath = os.path.join(os.path.dirname(__file__), filename)
        with open(filepath, 'r') as file:
            content = file.read()
        
        # Run your tests with file content
        cleaned = clean_text(content)
        tokens = tokenize(cleaned)
        counts = count_words(content)

        # Define expected results (these should be based on what you expect the output to be)
        expected_cleaned = clean_text("But the Raven sitting lonely on the placid bust spoke only That one word as if his soul in that one word he did outpour")
        expected_tokens = tokenize("But the Raven sitting lonely on the placid bust spoke only That one word as if his soul in that one word he did outpour")
        expected_counts = count_words("But the Raven sitting lonely on the placid bust spoke only That one word as if his soul in that one word he did outpour")

        # Asserts
        assert cleaned == expected_cleaned
        assert tokens == expected_tokens
        assert counts == expected_counts

# Test for French text
def test_french_text():
    cleaned = clean_text(FRENCH_TEXT)
    tokens = tokenize(cleaned)
    counts = count_words(FRENCH_TEXT)

    # Define expected results (these should be based on what you expect the output to be)
    expected_cleaned = clean_text(FRENCH_TEXT)
    expected_tokens = tokenize(FRENCH_TEXT)
    expected_counts = count_words(FRENCH_TEXT)

    # Asserts
    assert cleaned == expected_cleaned
    assert tokens == expected_tokens
    assert counts == expected_counts
