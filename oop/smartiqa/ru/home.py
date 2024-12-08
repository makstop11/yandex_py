class Human:
    defalt_name = ''
    default_age = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__money = 0
        self.__house = ''

    def info(self):
        print(self.name)
        print(self.age)
        print(self.__money)
        print(self.__house)

    @staticmethod
    def default_info():
        print(Human.default_age)
        print(Human.defalt_name)

    def make_deal(self, house, price):
        self.__money -= price
        self.__house = house

    def earn_money(self, money):
        self.__money += money

    def by_house(self):
        pass


class House:
    def __init__(self, area, price):
        self._area = area
        self._price = price

    def final_price(self, skidka):
        self._price -= skidka
