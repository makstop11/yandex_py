class Human:
    defalt_name = 'Неизвестно'
    default_age = 0

    def __init__(self, name=defalt_name, age=default_age):
        self.name: str = name
        self.age: int = age
        self.__money: int = 0
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
    def buy_house(self):
        self.__house

    def __str__(self) -> str:
        return (f'\nИмя: {self.name}'
                f'\nВозраст: {self.age}'
                f'\nВаш счёт: {self.__money}'
                f'\nВаш дом: {self.__house}')


class House:
    def __init__(self, area, price):
        self._area: int = area
        self._price: int = price

    def final_price(self, discount):
        self._price: int = self._price - (self._price / 100 * discount)
    def __str__(self) -> str:
        pass

class SmallHouse(House):
    def __init__(self):
        self._area: int = 40


if __name__ == '__main__':

    vasya:str = Human()
    # print(vasya)

    vasya.info()
    vasya.earn_money(500)
    vasya.info()
