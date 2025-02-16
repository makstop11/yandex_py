n = int(input())

x = 0
y = 1

while x < n:
    print(x)
    temp = y
    y = x + y
    x = temp

# temp = 1
# y = 1
# x = 1

# temp = 1
# y = 2
# x = 1


# temp = 2
# y = 3
# x = 2


# temp = 3
# y = 5
# x = 2


# temp = 5
# y = 7
# x = 3

# temp = 7
# y = 12
# x = 5

# temp = 12
# y = 19
# x = 7

# temp = 19
# y = 31
# x = 12

# temp = 31
# y = 50
# x = 19

# temp = 50
# y = 81
# x = 31

# temp = 81
# y = 131
# x = 50

# temp = 131
# y = 212
# x = 81
