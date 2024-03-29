fields = input()

rabbits_count = 0
while fields != 'Приехали!':
    if 'зайка' in fields:
        rabbits_count += 1
    fields = input()

print(rabbits_count)

# №2 - Решение с использованием моржового оператора

rabbits_count = 0
while (fields := input()) != 'Приехали!':
    if 'зайка' in fields:
        rabbits_count += 1

print(rabbits_count)
