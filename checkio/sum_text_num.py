#  text = "This picture is an oil on canvas painting by Danish artist Anna Petersen between 1845 and 1910 year"
text = "5 plus 6 is"

text = text.split()

summa = 0

for elem in text:
    if elem.isdigit():
        summa += int(elem)

print(summa)