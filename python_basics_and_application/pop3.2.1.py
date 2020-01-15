# Стандартные методы и функции для строк
s = input().strip()
a = input().strip()
b = input().strip()
cnt = 0
if a in s and a in b:
    print('Impossible')
else:
    while s.find(a) != -1:
        s = s.replace(a, b)
        cnt += 1
    print(cnt)