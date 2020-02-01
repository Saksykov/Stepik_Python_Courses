"""
Для разминки прочитайте последовательность, как описано на предыдущем шаге, и выведите её длину.
В последовательности могут быть пропуски (пустые строки).
"""
res = []
while True:
    x = input().strip()
    try:
        res.append(int(x))
    except ValueError:
        if x == ".":
            break
print(len(res))
