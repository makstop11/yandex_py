class MegaCat:
    LEGS: int = 4

    def change_legs_obj(self):
        self.LEGS = 10

    @classmethod
    def change_legs(cls):
        cls.LEGS = 6


class Phone:

    def __init__(self, color, model, os):
        self.color = color
        self.model = model
        self.os = os

    @classmethod
    def toy_phone(cls, color):
        toy_phone = cls(color, 'ToyPhone', None)
        # toy_phone_2 = Phone(color, 'ToyPhone', None)

        return toy_phone

    @staticmethod
    def model_hash(model):
        pass

    def check_sim(self, mobile_operator):
        pass


if __name__ == '__main__':
    mega_cat_1 = MegaCat()
    mega_cat_1.change_legs()

    print(mega_cat_1.__dict__)

    print(MegaCat.__dict__)
