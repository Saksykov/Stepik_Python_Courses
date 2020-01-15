# Итераторы и генераторы

def primes():
    i = 2
    while True:
        f = False
        if i == 2:
            yield i
        i += 1
        for a in range(2, i):
            if i % a == 0:
                f = True
                break
        if not f:
            yield i