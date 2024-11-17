class Factory:
    @staticmethod
    def build_sequence():
        return []

    def build_number(self, string):
        return int(string)


class Loader:
    @staticmethod
    def parse_format(string, factory):
        seq = factory.build_sequence()
        for sub in string.split(','):
            item = factory.build_sequence(sub)
            seq.append(item)
        return seq
