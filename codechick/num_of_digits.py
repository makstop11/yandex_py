# https://codechick.io/challenges/317

def num_of_digits(num):
    n = int(input())
    count = 0
    for i in range(n):
        if i == 0 or 1 or 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9:
            count += 1
        else:
            count
    print(count)
num_of_digits