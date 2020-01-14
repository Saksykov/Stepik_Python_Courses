# Simple continued fraction
a, b = (int(i) for i in input().split('/'))


def scf(n, m):
    if m == 1:
        print(n // m)
        return
    else:
        try:
            print(n//m, end=' ')
            scf(m, n % m)
        except ZeroDivisionError:
            return

scf(a, b)