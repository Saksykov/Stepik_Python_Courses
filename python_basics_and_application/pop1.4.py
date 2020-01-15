n = int(input())
d = {'global': {'parent': 'None', 'vargs': []}}
for i in range(n):
    fl = True
    cmd, nSp, arg = (str(o) for o in input().split())
    if cmd != 'get':
        if cmd == 'create':
            d[nSp] = {'parent': arg, 'vargs': []}
        else:
            d[nSp]['vargs'].append(arg)
    else:
        while fl:
            if nSp != 'None':
                for j in d[nSp]['vargs']:
                    if j == arg:
                        print(nSp)
                        fl = False
                        break
                nSp = d[nSp].get('parent')
            else:
                print('None')
                break


