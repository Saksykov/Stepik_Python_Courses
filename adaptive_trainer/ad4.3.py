s = ' abcdefghijklmnopqrstuvwxyz'
s = list(s)
n = int(input())
a = str(input().strip())
a = list(a)
res = []
for i in a:
    res.append(s[(s.index(i) + n) % 27])
print('Result:', '"' + ''.join(res) + '"')