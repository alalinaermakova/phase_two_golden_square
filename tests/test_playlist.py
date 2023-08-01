import pytest
from lib.playlist import *

"""
Given a track name 
Call the function to list tracks
"""

def test_add_one_track():
    user = Playlist()
    user.add("I do by G-idle")
    result = user.list_tracks()
    assert result == ["I do by G-idle"]

"""
Given two tracks
Call the function to list tracks
"""

def test_add_two_tracks():
    user = Playlist()
    user.add("I do by G-idle")
    user.add("Broken melody by NCT")
    result = user.list_tracks()
    assert result == ["I do by G-idle", "Broken melody by NCT"]

"""
Throwing exception "No tracks weren't added"
"""

def test_throeing_an_exception():
    with pytest.raises(Exception) as e:
        user = Playlist()
        user.list_tracks()
    assert str(e.value) == "No tracks weren't added"