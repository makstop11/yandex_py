class Car:
    pass


setattr(Car, "model", "Тойота")
setattr(Car, "color", "Белый")
setattr(Car, "number", "П111УУ777")

print(Car.__dict__["color"])
# print(Car.__dict__)
