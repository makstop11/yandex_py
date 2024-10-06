class Person:
    name: str = 'Сергей Балакирев'
    job: str = 'Программист'
    ity: str = 'Москва'

p1 = Person()

# TODO: На доработку
print(True if getattr(p1, 'job') else False)


# setattr() - установить атрибут
# getattr() - получить атрибут
# delattr() - удалить атрибут
# hasattr() - имеет ли атрибут
