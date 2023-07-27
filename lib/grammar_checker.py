def grammar_checker(txt):
    punctuation = ['!','?','.']
    
    if txt == None or txt == '':
        raise Exception("No string was given")
    elif any(c in punctuation for c in txt[-1]) and txt[0].isupper():
        return True
    else:
        return False
