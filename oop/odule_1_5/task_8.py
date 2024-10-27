class Cart:

    def __init__(self):
        self.goods = []

    def add(self, good):
        self.goods.append(good)

    def remove(self, index):
        self.goods.pop(index - 1)


if __name__ == "__main__":
        cart: Cart = Cart()
        cart.add(10)
        cart.add("some item")
        print(cart.goods)
        cart.remove(2)
        print(cart.goods)

        # TODO: дорешать
