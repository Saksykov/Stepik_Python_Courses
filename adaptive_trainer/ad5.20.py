# Game of life
n, m = (int(i) for i in input().split())
a, s = [], []
a = [[0 for i in range(m)] for j in range(n)]
s = [list(input().strip()) for i in range(n)]
for i in range(n):
    for j in range(m):
        cnt = 0
        for nI in range(i-1, i+2):
            for mJ in range(j-1, j+2):
                if nI == n:
                    nI = 0
                if mJ == m:
                    mJ = 0
                if s[nI][mJ] == 'X':
                    cnt += 1
        if s[i][j] == 'X':
            if 2 <= cnt-1 <= 3:
                a[i][j] = 'X'
            else:
                a[i][j] = '.'
        else:
            if cnt == 3:
                a[i][j] = 'X'
            else:
                a[i][j] = '.'
for i in range(n):
    for j in range(m):
        print(a[i][j], end='')
    print()