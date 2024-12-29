from typing import Optional


class Human:
    default_name: str = 'Неизвестно'
    default_age: int = 0

    def __init__(
            self,
            name: str = default_name,
            age: int = default_age
    ) -> None:
        self.name = name
        self.age = age
        self.__money: int = 0
        # self.__house: Optional['House'] = None
        self.__house: 'House' | None = None

    def info(self) -> None:
        print(self)

    @staticmethod
    def default_info() -> None:
        print(Human.default_age)
        print(Human.default_name)

    def __make_deal(self, house: 'House', price: int | float) -> None:
        self.__money -= price
        self.__house = house

    def earn_money(self, money) -> None:
        if money <= 0:
            print('Минимальная сумма 1 руб.')
        else:
            self.__money += money

    def buy_house(self, house: 'House', discount: int | float):
        house_price = house.final_price(discount)

        if self.__money < house_price:
            print('Недостаточно средств для покупки дома')
        else:
            self.__make_deal(house, house_price)

    def __str__(self) -> str:
        return (f'\nИмя: {self.name}'
                f'\nВозраст: {self.age}'
                f'\nВаш счёт: {self.__money} руб.'
                f'\nВаш дом: {self.__house}')


class House:
    def __init__(self, area: int, price: int) -> None:
        self._area = area
        self._price = price

    def final_price(self, discount: int | float) -> float:
        result: float = self._price - (self._price / 100 * discount)

        return result

    def __str__(self) -> str:
        return f'Площадь: {self._area} м2. Стоимость: {self._price} руб.'


class SmallHouse(House):
    def __init__(self, price: int) -> None:
        super().__init__(area=40, price=price)


if __name__ == '__main__':
    vasya: Human = Human('Василий', 22)
    vasya.info()
    vasya.earn_money(1_500_000)

    h_1 = House(30, 1_000_000)

    vasya.buy_house(h_1, 0)
    vasya.info()
