# Koch curve
n = int(input())
def koch(x):
    if x == 0:
        return
    koch(x - 1)
    print('turn 60')
    koch(x - 1)
    print('turn -120')
    koch(x - 1)
    print('turn 60')
    koch(x - 1)


koch(n)


