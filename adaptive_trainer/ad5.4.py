# Roman number to decimal
d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
n, res = 0, 0
a = list(input().strip())
for i in a:
    if n == 0:
        n = d.get(i)
        res += d.get(i)
    else:
        res += d.get(i)
        if n < d.get(i):
            res += - n*2
        n = d.get(i)
print(res)
