n = int(input())
x, y = 0, 0
for i in range(n):
    s = [str(j) for j in input().split()]
    if s[0] == 'север':
        y += int(s[1])
    elif s[0] == 'восток':
        x += int(s[1])
    elif s[0] == 'юг':
        y -= int(s[1])
    else:
        x -= int(s[1])
print(x, y)