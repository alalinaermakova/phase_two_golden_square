import pytest
from lib.diary_entry import *

"""
Giving the title and contents through
Format the content to show
"""

def test_diary_entry():
    my_diary = DiaryEntry('June 2023', "On tuesday walk the neighbour's dog")
    result = my_diary.format()
    assert result == "June 2023: On tuesday walk the neighbour's dog"


    """
    Giving the contents in string format
    Returns the number of words in a diary entry (integer)
    """

def test_diary_word_count():
    my_diary = DiaryEntry('June 2023', "On tuesday walk the neighbour's dog")
    result = my_diary.count_words()
    assert result == 6

    """
    Giving the word per minute that user can read
    Returns the estimate reading time in number of minutes/seconds (float)
    """

def test_diary_reading_time():
    my_diary = DiaryEntry('June 2023', "On tuesday walk the neighbour's dog")
    result = my_diary.reading_time(200)
    assert result == 0.03

    """
    Given the words per min and the number of minutes that user has to read
    Rturns a chunk of the content that user could read in the given number of minutes
    """

def test_reading_chunk():
    my_diary = DiaryEntry('June 2023', "On tuesday walk the neighbour's dog")
    result = my_diary.reading_chunk(200, 0.03) 
    assert result == "word word word word word word"



