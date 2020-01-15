# Стандартные методы и функции для строк
s = input().strip()
t = input().strip()
cnt, j = 0, 0
while j <= len(s) - len(t):
    if t in s[j:]:
        j += s[j:].find(t) + 1
        cnt += 1
    else:
        break
print(cnt)