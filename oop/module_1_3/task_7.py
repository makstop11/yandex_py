class Dictionary:
    rus: str = 'Питон'
    eng: str = 'Python'
    # rus_word: str = 'текст'


print(getattr(Dictionary, 'rus_word', False))
