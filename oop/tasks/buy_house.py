

class Human:
    default_name: str = "Неизвестный"
    default_age: int = 0

    def __init__(self, name=default_name, age=default_age):
        self.name = name
        self.age = age
        self.__money = 0
        self.__house = None

    def info(self):
        print(
            f"Имя: {self.name} Возраст: {self.age} "
            f"Баланс: {self.__money} Дом: {self.__house}"
        )

    @staticmethod
    def default_info():
        print(Human.default_name, Human.default_age)

    def __make_deal(self, house_obj, price):
        self.__money = self.__money - price
        self.__house = house_obj
        print(f"Вы приобрели дом: {house_obj}")

    def earn_money(self, amount):
        self.__money = self.__money + amount

    def buy_house(self, house, discount):
        house_price = house.final_price(discount)
        if self.__money < house_price:
            print("Недостаточно средств")
            return None
        self.__make_deal(house, house_price)


class House:
    def __init__(self, area, price):
        self._area = area
        self._price = price

    def final_price(self, sale):
        discount_sum = (self._price / 100) * sale
        result = self._price - discount_sum
        return result


class SmallHouse(House):
    def __init__(self, price):
        # House.__init__(self, area=40, price=price)
        super().__init__(area=40, price=price)


Human.default_info()
vasya = Human("Вася", 19)
# print(vasya.name)
# print(vasya.age)
# vasya.__house
# vasya.__make_deal()

vasya.info()

small = SmallHouse(100)
vasya.buy_house(small, 25)
vasya.earn_money(500)
vasya.buy_house(small, 25)

vasya.info()
