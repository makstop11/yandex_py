import sys


class StreamData:
    def create(self, fields, lst_values):
        for i, key in enumerate(fields):
            setattr(self, key, lst_values[i])

        if len(fields) != len(lst_values):
            return False


class StreamReader:
    FIELDS = ('id', 'title', 'pages')

    def readlines(self):
        lst_in = list(map(str.strip, sys.stdin.readlines()))
        sd = StreamReader()
        res = sd.create(self.FIELDS, lst_in)
        data, result = sd.readlines()
        return sd, res


# ---------------------------------------------------------------------------


# Enumerate() — это встроенная функция в Python, которая преобразует итерируемый объект в перечисляемый объект. 1
# Итерируемый объект — это любая последовательная коллекция элементов в виде списков, кортежей, словарей или строк. 1
# Функция создаёт объект-генератор, который генерирует кортежи, состоящие из двух элементов —
# индекса элемента и самого элемента. 2
