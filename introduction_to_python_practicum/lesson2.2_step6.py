"""
Напишите программу, которая будет вычислять n-ое число Фибоначчи. Число n, которое подается на вход программе,
может принимать значения от 0 до 20.
"""

n = int(input())
fib = [0, 1, 1]
if n < 3:
    print(fib[n])
else:
    i = 3
    while i <= n:
        fib.append(fib[i-1] + fib[i-2])
        i += 1
    print(fib[n])