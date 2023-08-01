class Playlist:

    def __init__(self):
        self.my_list = []

    def add(self, track):
        return self.my_list.append(track)

    def list_tracks(self):
        if len(self.my_list) == 0:
            raise Exception("No tracks weren't added")
        else:
            return self.my_list