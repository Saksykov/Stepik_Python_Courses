d = {}
cnt = 0
with open(r'D:\dataset_3363_4.txt', 'r') as r:
    for s in r:
        a = []
        n = 0
        s = s.strip()
        a = [str(i) for i in s.split(';')]
        for i in range(len(a)):
            if i == 0:
                d[cnt] = []
                n = cnt
                cnt += 1
            else:
                d[n] += [a[i]]

s = []
p1, p2, p3 = [], [], []
for i in range(len(d)):
    f = 0
    for j in range(len(d.get(i))):
        f += int(d.get(i)[j])
        if j == 0:
            p1 += [int(d.get(i)[j])]
        elif j == 1:
            p2 += [int(d.get(i)[j])]
        else:
            p3 += [int(d.get(i)[j])]
    s += [f / len(d.get(i))]
r1, r2, r3 = 0, 0, 0
for i in range(len(p1)):
    r1 += p1[i]
    r2 += p2[i]
    r3 += p3[i]

with open(r'D:\write.txt', 'w') as w:
    for i in s:
        w.write(str(i) + '\n')
    w.write(str(r1 / len(p1)) + " ")
    w.write(str(r2 / len(p2)) + " ")
    w.write(str(r3 / len(p3)))
