from lib.make_snippet import *

"""
Given a string and then returns the first 5 words
If it's not longer than that
"""

def test_5_words_string():
    result = make_snippet('Lorem ipsum dolor sit amet')
    assert result == 'Lorem ipsum dolor sit amet'

"""
Given string is longer than 5 words
Returns the first 5 words and '...'
"""

def test_longer_than_5_words():
    result = make_snippet('Lorem ipsum dolor sit amet ipsum')
    assert result == 'Lorem ipsum dolor sit amet...'