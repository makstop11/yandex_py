n = int(input())

x = 0
y = 1


while x < n:
    print(x)
    temp = y
    y = x + y
    x = temp
    print(x, y)


# temp = 1
# y = 1
# x = 1

# temp = 1
# y = 2
# x = 1


# temp = 2
# y = 3
# x = 1


# temp = 3
# y = 5
# x = 2


# temp = 5
# y = 8
# x = 3

# temp = 8
# y = 13
# x = 5

# temp = 13
# y = 21
# x = 8

# temp = 21
# y = 34
# x = 13

# temp = 34
# y = 55
# x = 21

# temp = 55
# y = 89
# x = 34

# temp = 89
# y = 144
# x = 55

# temp = 144
# y = 233
# x = 89
