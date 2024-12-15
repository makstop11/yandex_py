class Human:
    defalt_name = 'Неизвестно'
    default_age = 0

    def __init__(self, name=defalt_name, age=default_age):
        self.name = name
        self.age = age
        self.__money = 0
        self.__house = None

    def info(self):
        print(self)

    @staticmethod
    def default_info():
        print(Human.default_age)
        print(Human.defalt_name)

    # TODO: Не соответствует ТЗ.
    def make_deal(self, house, price):
        self.__money -= price
        self.__house = house

    def earn_money(self, money):
        self.__money += money

    # TODO: Параметры метода: ссылка на дом и размер скидки
    def by_house(self):
        pass

    def __str__(self) -> str:
        return (f'\nИмя: {self.name}'
                f'\nВозраст: {self.age}'
                f'\nВаш счёт: {self.__money}'
                f'\nВаш дом: {self.__house}')


class House:
    def __init__(self, area, price):
        self._area = area
        self._price = price

    def final_price(self, discount):
        # TODO: Неправильная реализация.
        self._price = discount


# TODO: SmallHouse

if __name__ == '__main__':
    # TODO: Добавить аннотация ко всем идентификатором.

    vasya = Human()
    # print(vasya)

    vasya.info()
    vasya.earn_money(500)
    vasya.info()
