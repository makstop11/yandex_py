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

if __name__ == '__main__':
    # vasya: Human = Human('Василий', 22)
    # vasya.info()
    # vasya.earn_money(1_500_000)
    #
    # h_1 = House(30, 1_000_000)
    #
    # vasya.buy_house(h_1, 0)
    # vasya.info()
