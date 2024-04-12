n = int(input())

print("А Б В")
for anya in range(1, n - 1):
    for borya in range(1, n - anya):
        vova = n - anya - borya
        if vova >= 1:
            print(anya, borya, vova)
