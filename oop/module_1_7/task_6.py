class Factory:
    @staticmethod
    def build_sequence() -> list:
        return []

    @staticmethod
    def build_number(string: str) -> int:
        return int(string)


class FloatFactory:
    @staticmethod
    def build_sequence() -> list:
        return []

    @staticmethod
    def build_number(string: str) -> float:
        return float(string)


class Loader:
    @staticmethod
    def parse_format(string, factory):
        seq = factory.build_sequence()
        for sub in string.split(','):
            item = factory.build_number(sub)
            seq.append(item)

        return seq


if __name__ == "__main__":
    print(Loader.parse_format("1234", Factory()))
    print(Loader.parse_format("1234", FloatFactory()))

    # @staticmethod - это декоратор
