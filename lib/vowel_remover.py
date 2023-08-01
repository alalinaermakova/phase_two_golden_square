class VowelRemover:
    def __init__(self, text):
        self.text = text
        self.vowels = ["a", "e", "i", "o", "u"]

    def remove_vowels(self):
        i = 0
        while i < len(self.text):
            if self.text[i].lower() in self.vowels:
                self.text = self.text[:i] + self.text[i+1:]
            else:
                i = i + 1
            print(f"i: {i}")
            print(f"length of text {len(self.text)}")
        
        return self.text

remover = VowelRemover('aeiuo')
print(remover.remove_vowels())
