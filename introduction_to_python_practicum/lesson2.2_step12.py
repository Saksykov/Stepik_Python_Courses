"""
Посчитайте сумму квадратов последовательности. Числа в ней могут быть вещественными.
"""

res = []
while True:
    x = input().strip()
    try:
        res.append(float(x))
    except ValueError:
        if x == ".":
            break
sum = 0
for i in res:
    sum += i*i
print(sum)
