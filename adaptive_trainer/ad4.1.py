a = str(input())
cnt = 1
c = ''
for i in range(len(a)):
    if a[i] == c:
        continue
    if len(a) > 1:
        for j in a[i+1::]:
            if a[i] == j:
                cnt += 1
            else:
                break
        if cnt > 1:
            print(str(cnt) + a[i], end='')
            c = a[i]
            cnt = 1
        else:
            print(a[i], end='')
            c = ''
    else:
        print(a[i])
