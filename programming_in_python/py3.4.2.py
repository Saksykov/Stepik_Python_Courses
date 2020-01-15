a = []
with open(r'D:\dataset_3363_3.txt', 'r') as r:
    for s in r:
        s = s.strip()
        a += [str(i).lower() for i in s.split()]

d = {}
mVal = 1
for i in a:
    if i in d:
        d[i] = d.get(i) + 1
        if d.get(i) > mVal:
            mVal = d.get(i)
    else:
        d[i] = 1

res = []
for i in d:
    if d.get(i) == mVal:
        res += [i]


res.sort()
print(res[0], mVal)

