class D:
    def __new__(cls, *args, **kwargs):
        obj = super().__new__(cls)
        print(f'Созданный объект: {id(obj)}')
        return obj

    def __init__(self):
        print(f'объект: {id(self)}')


d = D()

print(d)
# object
