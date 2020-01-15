n = int(input())
d = {}
s = []
for i in range(n):
    s = [str(o) for o in input().split(';')]
    for j in s[::2]:
        if j not in d:
            d[j] = [0, 0, 0, 0, 0]
        if s[1] < s[3]:
            if j == s[0]:
                d[j] = [d.get(j)[0] + 1, d.get(j)[1], d.get(j)[2], d.get(j)[3] + 1]
            else:
                d[j] = [d.get(j)[0] + 1, d.get(j)[1] + 1, d.get(j)[2], d.get(j)[3]]
        elif s[1] > s[3]:
            if j == s[0]:
                d[j] = [d.get(j)[0] + 1, d.get(j)[1] + 1, d.get(j)[2], d.get(j)[3]]
            else:
                d[j] = [d.get(j)[0] + 1, d.get(j)[1], d.get(j)[2], d.get(j)[3] + 1]
        else:
            d[j] = [d.get(j)[0] + 1, d.get(j)[1], d.get(j)[2] + 1, d.get(j)[3]]
for i in d:
    print(i, end=':')
    d[i] += [d.get(i)[1] * 3 + d.get(i)[2]]
    for j in d[i]:
        print(j, end=' ')
    print()



