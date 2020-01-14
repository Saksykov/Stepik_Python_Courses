# Transpose matrix
n, m = (int(i) for i in input().split())
a = [[int(i) for i in input().split()] for j in range(n)]
for i in range(m):
    for j in range(n):
        print(a[j][i], end=' ')
    print()
