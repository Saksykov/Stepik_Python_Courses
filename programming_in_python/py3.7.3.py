d = int(input())
a = []
for i in range(d):
    a += [str(input()).lower()]
l = int(input())
s = []
for i in range(l):
    s += [str(j).lower() for j in input().split()]
res = []
for i in s:
    cnt = 0
    for j in a:
        if i == j:
            cnt += 1
    if cnt == 0:
        res += [i]
for i in set(res):
    print(i)
