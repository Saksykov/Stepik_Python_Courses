s = ''.join([chr(i) for i in range(int(0x1f600), int(0x1f64f)+1)])
n = int(input())
a = str(input().strip())
res = []
for i in a:
    res.append(s[(s.index(i) + n) % 80])
print('Result:', '"' + ''.join(res) + '"')