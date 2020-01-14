n = int(input())
s = []
s.extend(str(i)*i for i in range(1, (n+3)//2))
a = ''.join(s)
for j in range(n):
    print(a[j], end=' ')