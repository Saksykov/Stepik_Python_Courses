# Jolly jumpers
s = ([int(i) for i in input().split()])
a = []
for i in range(len(s) - 1):
    a.append(abs(s[i] - s[i+1]))
if set(a) == set(range(1, len(s))):
    print('Jolly')
else:
    print('Not jolly')