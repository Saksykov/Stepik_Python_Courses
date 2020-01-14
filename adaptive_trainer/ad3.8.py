n = int(input())
a = [[0 for i in range(n)] for j in range(n)]
cnt = 1
l, r, h, d = 0, n, 0, n
ckl = 0
if n % 2 == 0:
    ckl = n // 2
else:
    ckl = n // 2 + 1
for i in range(ckl):
    for q in range(l, r):
        a[h][q] = cnt
        cnt += 1
    h += 1
    for w in range(h, d):
        a[w][r - 1] = cnt
        cnt += 1
    r -= 1
    for e in range(r - 1, l - 1, -1):
        a[d - 1][e] = cnt
        cnt += 1
    d -= 1
    for t in range(d - 1, h - 1, -1):
        a[t][l] = cnt
        cnt += 1
    l += 1
for i in range(n):
    for j in range(n):
        print(a[i][j], end=' ')
    print()
