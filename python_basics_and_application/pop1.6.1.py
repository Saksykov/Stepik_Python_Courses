d = {}
n = int(input())
for i in range(n):
    s = []
    s.extend(str(j) for j in input().split())
    if len(s) > 2:
        s.remove(':')
    if len(s) > 1:
        for o in range(1, len(s)):
            if s[0] in d:
                d[s[0]].append(s[o])
            else:
                d[s[0]] = []
                d[s[0]].append(s[o])
    else:
        d[s[0]] = []
al = []


def arr_per(ch):
    global al
    al.extend(d[ch])
    for I in d[ch]:
        arr_per(I)


m = int(input())
for i in range(m):
    s = []
    s.extend(str(j) for j in input().split())
    if s[0] == s[1]:
        print('Yes')
    else:
        arr_per(s[1])
        set(al)
        if al.count(s[0]) > 0:
            print('Yes')
        else:
            print('No')
    al.clear()

