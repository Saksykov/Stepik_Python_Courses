d = {}
s = input()
a = input()
for i in range(len(s)):
    d[s[i]] = a[i]

q = input()
w = input()
res = ''
for i in q:
    res += str(d.get(i))
req = ''
for i in w:
    for j in d:
        if i == d.get(j):
            req += str(j)
print(res)
print(req)

