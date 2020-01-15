objects = []
res = 0
for i in range(len(objects)):
    cnt = 0
    for j in range(i, len(objects)):
        if objects[i] is objects[j]:
            cnt += 1
    if cnt == 1:
        res += 1

print(res)