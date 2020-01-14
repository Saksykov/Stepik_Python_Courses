# Decimal number to Roman
d = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}
res = ''
n = input().strip()
for i in range(len(n)):
    a = int(n[i:])
    b = 10 ** (len(n[i:]) - 1)
    j = a // b
    if j % 5 == 4:
        res += d[b] + d[(j+1)*b]
    else:
        if j >= 5:
            res += d[b*5] + d[b] * (j-5)
        else:
            res += d[b] * j
print(res)