class Goods:
    title: str = "Мороженное"
    weight: int = 154
    tp: str = "Еда"  # тип продукта
    price: int = 1024


Goods.price = 2048
Goods.inflation = 100
print(Goods.__dict__)
