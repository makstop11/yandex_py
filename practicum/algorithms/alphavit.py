import string


# TODO: Нужны аннотации ко всем идентификаторам.


class Alphabet:
    def __init__(self, leng, letters):
        self.leng = leng
        self.letters = letters

    def print(self):
        print(self.letters)

    def letters_num(self):
        return len(self.letters)


class EngAlphabet(Alphabet):
    __letters_num: int = 26

    def __init__(self):
        super().__init__("En", string.ascii_uppercase)
        # Alphabet.__init__(self, lang, letters)

    def is_en_letter(self, char: str) -> bool:
        # return char in self.letters

        if char in self.letters:
            return True
        return False

    def letters_num(self):
        return self.__letters_num

# TODO: Дорешать
