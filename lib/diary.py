import math

class Diary:
    def __init__(self):
        self._entries = []

    def add(self, entry):
        self._entries.append(entry)

    def all(self):
        return self._entries

    def count_words(self):
        word_counts = [entry.count_words() for entry in self._entries]
        print(word_counts)
        return sum(word_counts)

    def reading_time(self, wpm):
        if self._entries == []:
            raise Exception("No entries added yet")
        word_count = self.count_words()
        return math.ceil(word_count / wpm)

    def find_best_entry_for_reading_time(self, wpm, minutes):
        if self._entries == []:
            raise Exception("No entries added yet")
        words_the_user_could_read = wpm * minutes
        most_readable = None
        longest_found_so_far = 0

        for entry in self._entries:
            if entry.count_words() <= words_the_user_could_read:
                if entry.count_words() > longest_found_so_far:
                    most_readable = entry
                    longest_found_so_far = entry.count_words()
        return most_readable

