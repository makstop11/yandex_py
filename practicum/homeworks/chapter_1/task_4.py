weight_gram: int = int(input())

tonne: float = weight_gram / 1000000
# tonne: float = weight_gram / 1E6
kilogram: float = weight_gram / 1000

print(f'Тонны: {tonne}')
print(f'Килограмм: {kilogram}')
