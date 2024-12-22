oklad = int(input())
procent = int(input())

nalog = oklad * procent / 100
summa = oklad - nalog

print(
    f"Ставка налога: {nalog}%"
    f"\nПолучаемая на руки сумма: {summa}р"
)
