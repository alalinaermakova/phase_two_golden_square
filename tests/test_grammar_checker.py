from lib.grammar_checker import *
import pytest

"""
    Given a string of 1 capitalized word and exclamaition mark.
    Returns True
"""
def test_one_uppercase_word(): 
    assert grammar_checker('Hello!') == True

"""
    Given a string of 1 capitalized word without any punctuation marks.
    Returns False
"""

def test_one_uppercase_word_no_puctuation():
    assert grammar_checker('Hey') == False

"""
    Given a string of a sentence witout capitalized letter and with full stop on the end.
    Returns False
"""

def test_no_uppercase_with_punctuation():
    assert grammar_checker('have a nice day.') == False

"""
    Given a string with all capitalized words no puctuation.
    Return False
"""

def test_sentence_uppercase_with_no_punctuation():
    assert grammar_checker('HAVE A NICE DAY') == False

"""
    Given an empty string.
    Raise Exception
"""

def test_empty_string():
    with pytest.raises(Exception) as error:
        grammar_checker('')
    assert str(error.value) == "No string was given"

"""
    Given None type value.
    Raises Exception
"""

def test_none_value():
    with pytest.raises(Exception) as error:
        grammar_checker(None)
    assert str(error.value) == "No string was given"