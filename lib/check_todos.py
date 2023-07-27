def check_todos(txt):
    if txt == '' or txt == None:
        raise Exception("No string was given")
    for s in txt:
        if "#TODO" in txt:
            return True
    else:
            return False
        