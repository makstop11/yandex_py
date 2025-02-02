# t = int(input())
#
# if t > 10:
#     s = 'Хорошая погода'
# else:
#     s = 'Плохая погода'
#
# print(s)

number: int = int(input())
if number % 4 == 0 and number % 2 == 0:
    print("ДА")
else:
    print("НЕТ")


def check_num(num: int) -> str:
    if num % 4 == 0 and num % 2 == 0:
        return "ДА"
    else:
        return "НЕТ"


if __name__ == "__main__":
    number: int = int(input())
    print(check_num(number))

