d={}
for i in range(1, 12):
    d[i] = []
with open(r'D:\dataset_3380_5.txt', 'r') as r:
    for i in r:
        s = [str(j) for j in i.strip().split()]
        q = int(s[0])
        d[q] += [s[2]]

for i in d:
    print(i, end=' ')
    a = 0
    if len(d[i]) == 0:
        print('-')
    else:
        for j in d[i]:
            a += int(j)
        print(a / len(d[i]))


