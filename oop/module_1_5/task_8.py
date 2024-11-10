class Cart:
    # TODO: Дорешать
    def __init__(self):
        self.goods = []

    def add(self, good):
        self.goods.append(good)

    def remove(self, index):
        self.goods.pop(index - 1)

    def get_list(self):
        print(self.goods)


class Table:
    pass


class TV:
    pass


class Notebook:
    pass


class Cup:
    pass


if __name__ == "__main__":
    cart: Cart = Cart()
    cart.add(10)
    cart.add("some item")
    print(cart.goods)
    cart.remove(2)
    print(cart.goods)
