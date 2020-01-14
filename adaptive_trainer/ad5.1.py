# Collatz conjecture or the 3n + 1 problem
n = int(input())
def collatz(i):
    print(i, end=' ')
    if i % 2 == 0:
        collatz(i//2)
    elif i == 1:
        return
    else:
        collatz(i * 3 + 1)
collatz(n)