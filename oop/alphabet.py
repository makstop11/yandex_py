
class Alphabet:
    def __init__(self, lang, letters):
        self.lang = lang
        self.letters = letters

    def print(self):
        print(self.letters)

    def letters_num(self):
        return len(self.letters)

class Tomato:
    states = ['зелёный','елёно-красный','красный']
    def __init__(self,_index,_stae):