1. Describe the problem
    User needs to keep track of their music. The need to add tracks and see a list of it.

2. Design the class interface

    class Playlist:

        def __init__(self):
            self.my_list = []

        def add(self, track):
            # Parameters:
            #   track: string
            # Saves the tracks to the self objects
            # Returns nothing
            pass

        def list_tracks(self):
            # Parameters: none
            # Returns a list of tracks
            # Side-effects:
            #   throwing an exception that tracks weren't added
            pass

3. Create Examples as Tests
    """
    Given a track name 
    Call the function to list tracks
    """

    user = Playlist()
    user.add("I do by G-idle")
    user.list_tracks() ==> ["I do by G-idle"]

    """
    Given two tracks
    Call the function to list tracks
    """

    user = Playlist()
    user.add("I do by G-idle")
    user.add("Broken melody by NCT")
    user.list_tracks() ==> ["I do by G-idle", "Broken melody by NCT"]

    """
    Throwing exception "No tracks weren't added"
    """

    user = Playlist()
    user.list_tracks() ==> "No tracks weren't added"