from pprint import pprint


class SingeltonFive:
    count = 0
    _LAST_OBJ = None
    _MAX_OBJECTS_COUNT: int = 5

    def __new__(cls, *args, **kwargs):
        if cls.count < cls._MAX_OBJECTS_COUNT:
            cls.count += 1

            current_obj = super().__new__(cls)
            cls._LAST_OBJ = current_obj
            return current_obj

        return cls._LAST_OBJ

    def __init__(self, name):
        self.name = name


elements: list[SingeltonFive] = []
for n in range(10):
    obj: SingeltonFive = SingeltonFive(str(n))
    elements.append(obj)

pprint(elements)
