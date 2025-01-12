import string


class Alphabet:
    def __init__(self, leng, letters) -> None:
        self.leng = leng
        self.letters = letters

    def print(self) -> None:
        print(self.letters)

    def letters_num(self) -> int:
        return len(self.letters)


class EngAlphabet(Alphabet):
    __letters_num: int = 26

    def __init__(self) -> None:
        super().__init__("En", string.ascii_uppercase)
        # Alphabet.__init__(self, lang, letters)

    def is_en_letter(self, char: str) -> bool:
        # return char in self.letters

        if char in self.letters:
            return True
        return False

    def letters_num(self) -> int:
        return self.__letters_num

    # TODO: Реализовать 6 пункт


if __name__ == '__main__':
    eng_1: EngAlphabet = EngAlphabet()
    eng_1.print()

    # TODO: Доработать Тесты 3, 4, 5, 6:
