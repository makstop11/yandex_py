n = int(input())

x = 0
y = 1

while x < n:
    print(x)
    temp = y
    y = x + y
    x = temp

# temp = 1
# y = 1         1
# x = 0

# temp = 1
# y = 2         2
# x = 1

# temp = 2
# y = 3         3
# x = 1

# temp = 3
# y = 5         4
# x = 2

# temp = 5
# y = 8         5
# x = 3

# temp = 8
# y = 11         6
# x = 3

# temp = 11
# y =  19        7
# x = 8

# temp = 19
# y = 30         8
# x = 11

# temp = 30
# y = 49         9
# x = 19

# temp = 49
# y = 79         10
# x = 30

# temp = 79
# y = 128         11
# x = 49

# temp = 128
# y =  207        12
# x = 79

# temp = 207
# y = 335         13
# x = 128
