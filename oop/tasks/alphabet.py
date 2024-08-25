class Alphabet:
    def __init__(self, lang: str, letters: str):
        self.lang = lang
        self.letters = letters

    def print(self):
        print(self.letters)

    def letters_num(self):
        return len(self.letters)


# TODO: Класс EngAlphabet
