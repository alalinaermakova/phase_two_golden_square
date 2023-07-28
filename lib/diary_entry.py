class DiaryEntry:
    def __init__(self, title, contents):
        self.title = title
        self.contents = contents
        pass

    def format(self):
        return f"{self.title}: {self.contents}"

    def count_words(self):
        word = self.contents.split()
        return len(word)

    def reading_time(self, wpm):
        words = self.contents.split()
        word_count = len(words)
        return word_count / 200
    
    def reading_chunk(self, wpm, minutes):
        chunk_of_words = int(wpm * minutes)
        text = " ".join(["word" for i in range(1, chunk_of_words +1)])
        return text

            
