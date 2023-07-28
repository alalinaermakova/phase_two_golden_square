from lib.grammar_stats import *
import pytest

"""
Giving the string of text
Returns boolean value True
"""
def test_grammar_stats_true():
    checker = GrammarStats()
    result = checker.check("Hello!")
    assert result == True

"""
Giving the string of text
Returns boolean value False
"""

def test_grammar_stats_false():
    checker = GrammarStats()
    result = checker.check("Hello")
    assert result == False

"""
Calculating the percentage of texts checked
Returns the integer
"""
def test_grammar_persentage():
    checker = GrammarStats()
    result = checker.check("Hello!")
    result = checker.check("Hello")
    result = checker.check("Hey.")
    result = checker.check("Allo?")
    result = checker.percentage_good()
    assert result == 75

"""
Given an empty string.
Raise Exception
"""
def test_grammar_empty_list():
    with pytest.raises(Exception) as error:
        checker = GrammarStats()
        checker.check("")
    assert str(error.value) == "No string was given"

"""
Given None type value.
Raises Exception
"""

def test_grammar_empty_list():
    with pytest.raises(Exception) as error:
        checker = GrammarStats()
        checker.check(None)
    assert str(error.value) == "No string was given"