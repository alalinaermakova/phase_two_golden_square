class GrammarStats:
    def __init__(self):
        self.my_texts = []

    def check(self, text):
        punctuation = ['!','?','.']
        if text == None or text == '':
            raise Exception("No string was given")
        elif any(c in punctuation for c in text[-1]) and text[0].isupper():
            self.my_texts.append(1)
            return True
        else:
            self.my_texts.append(0)
            return False

    def percentage_good(self):
        passed_check = self.my_texts.count(1)
        res = (100 * passed_check) / len(self.my_texts)
        return int(res)