# TODO: Подвиг 7

class Dictionary:
    rus: str = 'Питон'
    eng: str = 'Python'

print(getattr(Dictionary, 'rus_word', False))
