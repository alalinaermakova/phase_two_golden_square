from lib.music_library import MusicLibrary
from lib.track import Track

""" 
Iitially
There are no tracks
""" 

def test_initially_has_no_tracks():
    library = MusicLibrary()
    assert library.all() == []
"""
We can create a new track
We can get its title and artist back
""" 

def test_construct_track_and_get_title_and_artist():
    track = Track("My Title", "My Artist")
    assert track.title == "My Title"
    assert track.artist == "My Artist"

def test_formats_title_and_artist():
    track = Track("My Title", "My Artist")
    assert track.format() == "My Title by My Artist"

"""
When we add two tracks
And we search for a title of one of the tracks
We get the matching track back
"""
def test_searches_by_title():
    library = MusicLibrary()
    track_1 = Track("My Title 1", "My Artist 1")
    track_2 = Track("My Title 2", "My Artist 2")
    library.add(track_1)
    library.add(track_2)
    assert library.search_by_title("My Title 2") == [track_2]

"""
When we add two tracks
And we search for a word in the title
We get the matching track back
"""

def seraches_by_part_of_the_title():
    library = MusicLibrary()
    track_1 = Track("My Title 1", "My Artist 2")
    track_2 = Track("My Title 3", "My Artist 4")
    library.add(track_1)
    library.add(track_2)
    assert library.search_by_title("1") == [track_1]

"""
When we add two tracks
And we search for a word not in any track title
We get an empty list back
"""

def search_for_non_excisting_file():
    library = MusicLibrary()
    track_1 = Track("Always The Hard Way", "Terror")
    track_2 = Track("Higher Place", "Malevolence")
    library.add(track_1)
    library.add(track_2)
    assert library.search_by_title("zzz") == []

