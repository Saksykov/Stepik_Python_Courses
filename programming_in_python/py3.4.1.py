a = []
with open(r'D:\dataset_3363_2.txt', 'r') as r:
    for s in r:
        s = s.strip()
        a += [str(i) for i in s.split()]

b = []
for i in a:
    z = []
    x = []
    for j in range(len(i)):
        if j == len(i)-1:
            z += [i[j]]
            f = ''.join(z)
            g = ''.join(x)
            b += [g * int(f)]
        elif i[j] < 'A':
            z += [i[j]]
        elif len(x) == 0:
            x += [i[j]]
        else:
            f = ''.join(z)
            g = ''.join(x)
            b += [g * int(f)]
            x.clear()
            x += i[j]
            z.clear()

with open(r'D:\write.txt', 'w') as w:
    for i in b:
        w.write(i)
