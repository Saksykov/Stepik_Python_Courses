s = input().strip()
s = list(s)
res = ''
n = ''
for i in s:
    if str(i).isdigit():
        n += str(i)
    else:
        if n.isdigit():
            res += str(i) * int(n)
            n = ''
        else:
            res += str(i)
print(res)