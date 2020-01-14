a = str(input())
b = str(input())
x = []
for i in range(len(a)):
    z = 0
    if i + len(b) <= len(a):
        z = a[i::].find(b) + i
        if i == z:
            x += [z]
    else:
        break
if len(x)>0:
    for j in x:
        print(j, end=' ')
else:
    print(-1)
