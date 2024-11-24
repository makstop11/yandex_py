class Car:
    def run(self):
        print("Запускаем машину + топливный бак")


class ElectroCar(Car):
    def run(self):
        print("Запускаем машину + электродвигатель")


if __name__ == '__main__':
    car = Car()
    electro = ElectroCar()

    car.run()
    electro.run()
