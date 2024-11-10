class SingeltonFive:
    name = ''
    count = 0

    def __new__(cls, *args, **kwargs):
        if cls.count <= 0:
            cls.count += 1

    def __init__(self, name):
        self.name = name


objs = [SingeltonFive(str(n)) for n in range(10)]
