from lib.check_todos import *
import pytest

"""
    Given a string of a sentence that includes #TODO
    Returns True
"""

def test_string_with_todo():
    assert check_todos('#TODO: Record the video for this challenge') == True

"""
    Given a string of a sentence that includes # and some words
    Returns False
"""

def test_string_without_todo():
    assert check_todos("#Make a list") == False

"""
    Given a string of a sentence to do
    Returns False
"""

def test_string_with_task():
    assert check_todos("to do dishes") == False

"""
    Given an empty string
    Raise Exception
"""

def test_empty_string():
    with pytest.raises(Exception) as error:
        check_todos('')
    assert str(error.value) == "No string was given"

"""
    Given a None value
    Raise Exception "No string was given"
"""

def test_none_value():
    with pytest.raises(Exception) as error:
        check_todos(None)
    assert str(error.value) == "No string was given"

