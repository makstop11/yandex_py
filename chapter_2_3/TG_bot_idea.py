import random
import time
import math


# random.seed(int(time.time()))

# Функция приветствие
def hallo_game():
    hallo = random.choice(['\n👋👋👋 Привет Друг❗️ Давай сыграем в числовую угадайку❓❓❓\n',
                           '\n👋 Привет❗️ Добро пожаловать в числовую угадайку❗️\n',
                           '\nПриветствую 👋👋👋❗️❗️❗️ Желаешь сыграть в числовую угадайку❓\n',
                           '\n👋Хей-Хей❗️❗️❗️👋 Как на счет игры в числовую угадайку❓😉\n'])
    print(hallo)
    time.sleep(2)


# Функция выбора игры
def choice_game():
    print('       👉...---===У нас два режима игры===---...👈',
          '👉1) Ты угадываешь число, которое загадал компьютер  (1👈',
          '👉2) Ты загадываешь число, а компьютер его угадывает (2👈',
          '👉3) Выход из игры', sep='\n')
    time.sleep(1)
    # Предлагаем выбрать режим игры или выйти
    print('\n Введи 1 или 2 для выбора режима игры, или 3 для выхода')
    exam_list = ['1', '2', '3']  # для исключения неверного ввода

    # Проверяем корректность ввода
    while True:
        mode = input('👉: ')
        if mode not in exam_list:
            print(random.choice(['ты должен ввести 1, 2 или 3', 'Давай не будем тупить... Введи 1, 2 или 3']))
        else:
            break

    # Возвращаем номер режима
    if mode == '1':
        return 1
    elif mode == '2':
        return 2
    else:
        return False


# Функция запуска первого или второго режима
def start_game(number_game):
    if number_game == 1:
        start_user_game()
    elif number_game == 2:
        start_computer_game()


# Проверяем корректность ввода числа
def is_valid_digit(digit):
    # Проверяем, ввел ли пользователь число а не буквы или символы
    while True:
        if not digit.isdigit():
            print('❌Неет❌, тебе нужно ввести цифру, а не букву или символ =)')
            print('Давай попробуем еще раз')
            digit = input('👉: ')
        else:
            break
    # Возвращаем число
    return int(digit)


# Получаем от игрока кол-во попыток
def get_popit_user():
    time.sleep(1)
    print('И так, сколько тебе понадобится попыток, чтобы отгадать число❓')

    # Пользователь вводит число, и сразу идет проверка на корректность вода (цифра/буква/символ)
    popit = is_valid_digit(input('👉: '))  # получаем тип данных int

    # Кол-во попыток должно быть больше 0
    while True:
        if 0 >= popit:
            print('❌Неет❌, тебе нужно ввести число от 1 и выше☝️')
            print('Давай попробуем еще раз')
        else:
            break
    # Возвращаем число от игрока
    return popit


# Получаем от игрока диапазон для игры
def get_range_user_comp():
    time.sleep(1)
    print('\nХорошо, давай определим диапазон чисел😃')
    time.sleep(1)
    print('\nКакое будет начальное число❓')
    left_range = is_valid_digit(
        input('👉: '))  # Пользователь вводит число, и сразу идет проверка на корректность вода (цифра/буква/символ)

    time.sleep(1)
    print('Какое будет конечное число❓')
    while True:
        right_range = is_valid_digit(
            input('👉: '))  # Пользователь вводит число, и сразу идет проверка на корректность вода (цифра/буква/символ)
        if right_range <= left_range:
            print('❌Неет❌, конечное число должно быть больше начального‼️)')
            print('Давай попробуем еще раз')
        else:
            break
    # Возвращаем два значения int для указания диапазона
    return left_range, right_range


# Функция игры пользователя
def user_game(popit, l_range, r_range):
    mystery = random.randint(l_range, r_range)  # получаем два значения для диапазона
    count_popit = 0  # счетчик попыток
    time.sleep(1)
    print('\n⏱⏱⏱ДУМАЮ⏱⏱⏱')
    time.sleep(2)
    print('😈Всё, я загадал число❗️😈')
    time.sleep(1)
    for _ in range(popit):  # кол-во итераций == кол-ву введенных пользователем попыток
        print('😈Отгадывай😈')
        clue = is_valid_digit(
            input('👉: '))  # Пользователь вводит число, и сразу идет проверка на корректность вода (цифра/буква/символ)
        time.sleep(1)

        # Если игрок отгадал число, сразу поздравляем и заканчиваем игру
        if clue == mystery:
            count_popit += 1
            win = random.choice(['\n🎇🎇🎇УРА❗️❗️❗️ ТЫ ОТГАДАЛ❗️❗️❗️🎇🎇🎇',
                                 '\n🎇КРУТО❗️ ТЫ СПРАВИЛСЯ❗️🎇',
                                 '\n🎇🎇🎇НУ НИФИГА СЕБЕ❗️❗️❗️ КАК ТЫ ОТГАДАЛ❓❓❓🎇🎇🎇'])
            print(win)
            time.sleep(1)
            print(f'Ты угадал за {count_popit} попыток')
            count_popit += 1
            break

        # Если введенное число меньше загаданного
        elif mystery < clue:
            bigger = random.choice(['❌НЕТ❌', 'А вот и не правильно😝', 'Подумай хорошенько❗️'])
            print(bigger, 'Загаданное число меньше ➖')
            count_popit += 1

        # Если введенное число больше загаданного
        elif mystery > clue:
            smaller = random.choice(['❌🧐❌', '😌НЕА😌', 'Пошевели мозгами❗️🤪🤪🤪'])
            print(smaller, 'Загаданное число больше➕')
            count_popit += 1
    # Кол-во итераций (попыток) закончилось. Пользователь не отгадал число
    else:
        not_win = random.choice(['🤥Ты пролетел как фанера над Парижем❗️🤥',
                                 '😈ХА-ХА-ХА, тебе никогда не победить меня❗️😈'])
        print(not_win, f'Я загадал число {mystery}😝', sep='\n')


# Функция игры компьютера
def computer_game(l_range, r_range):
    # Формулма определения кол-ва попыток
    pop = math.ceil(math.log(r_range, 2))
    time.sleep(1)

    # Болтология с компьютером
    print(f'Ты выбрал диапазон от {l_range} до {r_range}')
    time.sleep(1)
    print(random.choice(['Хмммм...', 'Нуууу...', 'Иииии...']))
    time.sleep(2)
    print(f'Я угадаю твое число за {pop} попыток❗️🔮')
    time.sleep(2)
    start = input('Напиши "да" или "+", если загадал число\n👉: ')
    start_list = ['да', 'д', '+', 'Да', 'ДА', 'Д', 'дА', 'lf', 'L', 'Lf', 'LF', 'lF']
    count_pop = 0

    while True:  # Проверяем ответ пользователя
        if start not in start_list:
            print('Я же попросил ввести "да" или "+"')
            start = input('Давай еще раз\n👉: ')
        else:
            break

    print('Класс❗️ Поехали 🚘🚘🚘')
    for _ in range(pop):  # Кол-во итераций == кол-ву попыток указанных компьютером
        middle = (l_range + r_range) // 2  # Первое число ==  середине диапазона
        time.sleep(1)

        print(random.choice(['\n⏱⏱⏱ДУМАЮ⏱⏱⏱', '\nТааак, cейчас...']))
        time.sleep(2)
        print(random.choice(['🤓Ты загадал число', '😎Думаю, что твое число:', '🤖Это число']), middle)

        time.sleep(1)
        answer = input('Напиши "да", если я угадал, "+" если твое число больше, и "-" если твое число меньше\n👉: ')

        while True:
            if answer not in start_list and answer != '+' and answer != '-':
                print('\n❌❌❌Ну нет уж, ты должен был ввести "да", "+" или "-" \n Давай еще раз... \n')
                answer = input('Пиши...👉: ')
            else:
                break
        time.sleep(1)

        if answer in start_list and answer != '+':  # Если пользователь подтверждает угадывание числа, завершаем игру, а компьютре радуется победе
            count_pop += 1
            print(random.choice(['Еееессс, я угадал с', 'Вот так❗️ ДА❗️ Учииись😝 Я угадал с']), count_pop,
                  'попытки❗️❗️❗️')
            break

        elif answer == '+':  # Если загаданное число больше
            time.sleep(1)
            print(random.choice(['Ну ладно😡... больше так больше😡...',
                                 'Таак...', 'Хммм🧐 А может...',
                                 'Ты серьезно⁉️ Ну хорошо...']))
            count_pop += 1
            l_range = middle + 1

        elif answer == '-':  # Если загаданное число меньше
            time.sleep(1)
            print(random.choice(['Ах ты ж... Ладно, попробую еще...😤😤😤',
                                 'Ну как же тааак❓❓ БЛИН 🤬🤬🤬',
                                 '😶Ээээхххх...']))
            count_pop += 1
            r_range = middle - 1
    else:  # Вообще компьютер не мог не угадать число. Но никто и не говорил, что нельзя обманывать)))
        time.sleep(1)
        print(f'ТЫ меня обманул, и по этому я не смог отгадать число за {pop} попыток 😭😭😭\n')


# Запуска игры пользователя
def start_user_game():
    # Задаем диапазон
    star_dig, last_dig = get_range_user_comp()
    # Задаем кол-во попыток
    popit = get_popit_user()

    # Запускаем игру, где ползователь должен отгадать число
    user_game(popit, star_dig, last_dig)
    time.sleep(1)


# Запуска игры компьютера
def start_computer_game():
    # Задаем диапазон
    start_dig, last_dig = get_range_user_comp()

    # Запускаем игру, где компьютер должен отгадать число
    computer_game(start_dig, last_dig)

    time.sleep(1)


# функция повторения игры
def replay_game():
    print()
    print(random.choice(['😊Сыграем еще разок❓😊',
                         '😊Может еще поиграем❓😊',
                         '😊Желаешь еще раз сыграть❓😊']))

    answer = input('напиши "да" или "нет" тут 👉: ')
    answer_list_yes = ['да', 'д', 'Да', 'ДА', 'Д', 'дА', 'lf', 'L', 'Lf', 'LF', 'lF']
    answer_list_no = ['НЕТ', 'Нет', 'нет', 'Н', 'н', '-', 'N', 'NO', 'No', 'no', 'n', 'YTN', 'Ytn', 'ytn', 'net']

    while True:  # Проверяем введенный ответ
        if answer not in answer_list_yes and answer not in answer_list_no:
            print('❌❌❌❗️❗️❗️Ты втираешь мне какую то дичь❗️❗️❗️❌❌❌')
            answer = input('напиши "да" или "нет" тут 👉: ')
        else:
            break

    if answer in answer_list_yes:  # Если пользователь желает сыграть еще раз
        print(random.choice(['\n🎆Отлично❗️ Продолжаем❗️🎆\n',
                             '\n👏Что ж, Играем дальше👏\n',
                             '\n😂Ааа, понравилось❓ На давай❗️😂\n',
                             '\n🚀Ну давай❗️ Поехали🚀\n']))
        return True
    elif answer in answer_list_no:  # Если пользователь решил больше не играть
        return False


# Функция вывод текст прощания
def bay_bay():
    print(random.choice(['\nНу и ладно❗️ Ну и пожалуйста❗️😔',
                         '\nЗахочешь поиграть еще, приходи❗️👋👋👋',
                         '\n💥💥💥ДО СКОРЫХ ВСТРЕЧЬ❗️💥💥💥']))


# Поставь лайк)))
def get_like():
    print()
    words_1 = '*    если понравилось      *'
    words_2 = '* ставь лайк под комментом *'
    words_l1 = list(words_1)
    words_l2 = list(words_2)
    for i in range(28):
        print('*', end='')
        time.sleep(0.01)
    print()
    for i in range(28):
        time.sleep(0.01)
        print(words_1[i], end='')
    print()
    for i in range(28):
        time.sleep(0.01)
        print(words_2[i], end='')
    print()
    for i in range(28):
        time.sleep(0.01)
        print('*', end='')


# Функция запуска программы
def main():
    # Начинаем игру с приветствия
    hallo_game()
    while True:
        # Выбираем режим
        num_game = choice_game()
        if not num_game:  # Если пользователь выбрал 3й пункт (Выход из игры), завершаем цикл и переходим к функции вывода текста прощания
            break
        start_game(num_game)  # Запускается игра согласно выбранному режиму

        # Предлагаем повторить всё с самого начала, начиная с выбора режима
        time.sleep(1)
        if replay_game():
            continue
        else:
            break
    # Прощаемся и просим поставить лайк
    bay_bay()
    get_like()


# Точка входа (Запуск программы)
if __name__ == '__main__':
    main()
