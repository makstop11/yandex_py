players_count = int(input())

names = []
for _ in range(players_count):
    player_name = input()
    names.append(player_name)

    # TODO: 1. Этот код будет вне цикла.
    #  2. Метод sort() ничего не принимает.
    #  3. Метод sort() возвращает None, так что
    #  присваивать результат этот метода нет смысла
    player_name = names.sort(names)

# TODO: 4. Здесь выведешь первый элемент списка names
print(player_name)
