n, m = (int(i) for i in input().split())
fil = []
for i in range(n):
    s = str(input())
    s = list(s)
    fil.append(s)
res = [[0] * m for i in range(n)]
for i in range(n):
    for j in range(m):
        cnt = 0
        if fil[i][j] == '*':
            res[i][j] = '*'
        else:
            for fI in range(i-1, i+2):
                if 0 <= fI < n:
                    for fJ in range(j-1, j+2):
                        if 0 <= fJ < m:
                            if fil[fI][fJ] == '*':
                                cnt += 1
            res[i][j] = cnt
for i in range(n):
    for j in range(m):
        print(res[i][j], end='')
    print()