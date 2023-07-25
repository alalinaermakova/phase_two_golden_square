from lib.count_words import *

"""
Given a string as an argument,
Returns number of words
"""

def test_count_words_in_string():
    result = count_words('Lorem ipsum dolor sit amet')
    assert result == 5