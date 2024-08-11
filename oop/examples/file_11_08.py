class Human:
    # Свойство, поле, атрибут
    HAND: int = 2
    FOOT: int = 2

    # Метод
    def hello(self):
        print('Привет!')


class Student(Human):
    GRADE_BOOK: list = []

    def grade(self):
        print('Я отличник!')

    # Переопреление родительского метода
    def hello(self):
        print('Хеллоу, я студент!')


class Employee(Human):
    pass


# экземпляр, объект
vasya = Human()
vasya.hello()

student_1 = Student()
student_1.hello()
student_1.grade()
