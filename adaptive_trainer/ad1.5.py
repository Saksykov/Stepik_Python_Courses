a = []
a.extend([str(i) for i in input().split()])
cnt = 0
for i in a:
    if i == 'A':
        cnt += 1
print('{0:.2f}'. format(cnt/len(a)))