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
# x = 1

# temp = 1
# y = 2         2
# x = 1

# temp = 2
# y = 3         3
# x = 2

# temp = 3
# y = 5         4
# x = 3

# temp = 5
# y = 8         5
# x = 5

# temp = 8
# y = 13         6
# x = 8

# temp = 13
# y = 21         7
# x = 13

# temp = 21
# y = 34         8
# x = 21

# temp = 34
# y = 55         9
# x = 34

# temp = 55
# y = 89         10
# x = 55

# temp = 89
# y = 144         11
# x = 89

# temp = 144
# y = 233         12
# x = 144

# temp = 233
# y = 377         13
# x = 233
