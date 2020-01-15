er = {}
obj = 'obj'
n = int(input())
for i in range(n):
    s = []
    s.extend([str(j) for j in input().split()])
    if len(s) > 1:
        s.remove(':')
        for o in range(1, len(s)):
            if s[o] in er:
                er[s[o]].append(s[0])
            else:
                er[s[o]] = []
                er[s[o]].append(s[0])
    else:
        if obj in er:
            er[obj].append(s[0])
        else:
            er[obj] = []
            er[obj].append(s[0])
al = []


def arCh(per):
    global al
    al.extend(er[per])
    for I in er[per]:
        if I in er:
            arCh(I)


m = int(input())
t = []
for i in range(m):
    t.append(str(input().strip()))
res, pr = [], []
cop = t.copy()
for j in t:
    if t[t.index(j):].count(j) > 1:
        for k in t[len(t)-1: t.index(j): -1]:
            if j == k:
                res.append(k)
                t.remove(k)
    if j in er:
        arCh(j)
        for o in al:
            if t[t.index(j):].count(o) > 0:
                res.append(o)
                for h in range(t[t.index(j):].count(o)):
                    t.remove(o)
    al.clear()
for i in cop[::-1]:
    if i in res and i not in pr:
        pr.insert(0, i)
for j in pr:
    print(j)