class AbstractClass:
    def __new__(cls, *args, **kwargs):
        return 'Ошибка: нельзя создавать объекты абстрактного класса' \
               'Error: You cannot create abstract class objects'
