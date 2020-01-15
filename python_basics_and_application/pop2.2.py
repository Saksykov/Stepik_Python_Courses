import datetime

s = []
s.extend([int(i) for i in input().split()])
d = datetime.date(s[0], s[1], s[2])
day = int(input())
delta = datetime.timedelta(days=day)
res = d + delta
print(res.year, res.month, res.day)
