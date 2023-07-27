def reading_time_manager(txt):
    if txt != None:
        words = txt.split()
        word_count = len(words)
        res = word_count / 200
        if res < 1:
            return f"{res} seconds"
        elif res == 1:
            return f"{res} minute"
        else:
            return f"{res} minutes"
    raise Exception('No text to count time')