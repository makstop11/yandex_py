players_count = int(input())

names = []
for _ in range(players_count):
    player_name = input()
    names.append(player_name)
names = sorted(names)

print(names[0])
