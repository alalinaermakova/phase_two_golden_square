from lib.new_diary_entry import DiaryEntry

"""
When I initialise with a title and contents
I can get title and contents back
"""

def test_constructs_and_gets_title_and_contents():
    diary_entry = DiaryEntry("My Title", "My Contents")
    assert diary_entry.title == "My Title"
    assert diary_entry.contents == "My Contents"

"""
When I initialise with a five word contents
Then #count_words should return five
"""

def test_count_words_return_word_count_of_contants():
    diary_entry = DiaryEntry("My Title", "one two threee four five")
    assert diary_entry.count_words() == 5

"""
When I initialise with a five word contents
Then #reading_time with a wpm of 2 should return 3
"""

def test_reading_time():
    diary_entry = DiaryEntry("My Title", "one two threee four five")
    assert diary_entry.reading_time(2) == 3

"""
When I initialise with 5-word contents
Then, at first, #reading_chunk should return the first chunk
    readable in the time
"""

def test_reading_first_chunk():
    diary_entry = DiaryEntry("My Title", "one two threee four five")
    assert diary_entry.reading_chunk(2, 1) == "one two"

"""
Whaen I initialise with a 5-word contents
Then, on second call, #reading_chunk should return the second chunk
    readable in the time
"""

def test_reading_second_chunk():
    diary_entry = DiaryEntry("My Title", "one two three four five")
    diary_entry.reading_chunk(2, 1)
    assert diary_entry.reading_chunk(2, 1) == "three four" 

"""
Whaen I initialise with a 5-word contents
Then, on second call, #reading_chunk should return the final chunk
    readable in the time
"""

def test_readable_chunk_third_chunk():
    diary_entry = DiaryEntry("My Title", "one two three four five")
    diary_entry.reading_chunk(2, 1)
    diary_entry.reading_chunk(2, 1)
    assert diary_entry.reading_chunk(2, 1) == "five"

"""
When I initialise with a five-words content
Then on the fourth call, #reading_chunks should start again from the beginning
"""

def test_readable_chunk_fourth_chunk():
    diary_entry = DiaryEntry("My Title", "one two three four five")
    diary_entry.reading_chunk(2, 1)
    diary_entry.reading_chunk(2, 1)
    diary_entry.reading_chunk(2, 1)
    assert diary_entry.reading_chunk(2, 1) == "one two"

"""
When I initialise with a six-words content
Then on the fourth call, #reading_chunks should start again from the beginning
"""

def test_readable_chunk_fourth_chunk_six_words():
    diary_entry = DiaryEntry("My Title", "one two three four five six")
    diary_entry.reading_chunk(2, 1)
    diary_entry.reading_chunk(2, 1)
    diary_entry.reading_chunk(2, 1)
    assert diary_entry.reading_chunk(2, 1) == "one two"