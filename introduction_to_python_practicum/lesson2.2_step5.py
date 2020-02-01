"""
Простое число делится без остатка только на 1 и на само себя.
Напишите программу, которая прочитает число и выведет "prime" если число простое и
"composite" в противном случае (без кавычек).
"""

x = int(input())
j = x - 1
f = True
while j > 1:
    if x % j != 0:
        j -= 1
        continue
    else:
        f = False
        break
if f:
    print("prime")
else:
    print("composite")
