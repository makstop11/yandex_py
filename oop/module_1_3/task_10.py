class Person:
    name: str = 'Сергей Балакирев'
    job: str = 'Программист'
    ity: str = 'Москва'

p_1 = Person()

print(True if getattr(p_1, 'job') else False)
print(hasattr(p_1, 'job'))

# setattr() - установить атрибут
# getattr() - получить атрибут
# delattr() - удалить атрибут
# hasattr() - имеет ли атрибут
