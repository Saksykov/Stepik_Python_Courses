# Hanoi Tower
n = int(input())


def hanoi(i, a, b):
    if i == 1:
        print(str(a) + ' - ' + str(b))
    else:
        c = 6 - a - b
        hanoi(i-1, a, c)
        print(str(a) + ' - ' + str(b))
        hanoi(i-1, c, b)


hanoi(n, 1, 3)