def make_snippet(my_str):
    res = my_str.split()
    if len(res) <= 5:
        return my_str
    elif len(res) > 5:
        return ' '.join(res[:5]) + "..."
