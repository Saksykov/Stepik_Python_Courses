'''
Вам дано описание наследования классов в формате JSON.
Описание представляет из себя массив JSON-объектов, которые соответствуют классам. У каждого JSON-объекта
есть поле name, которое содержит имя класса, и поле parents, которое содержит список имен прямых предков.
'''
import json

js = json.loads(input().rstrip())
d = {}
res = []
n = ''
for i in js:
    if i['name'] not in d:
        d[i['name']] = []
    for j in i['parents']:
        if j not in d:
            d[j] = [i['name']]
        else:
            d[j].append(i['name'])


def par(name):
    global d, n
    for q in d[name]:
        if q not in d[n]:
            d[n].append(q)
        par(q)
    return len(d[name])


for j in d:
    n = j
    res.append(j + ' : ' + str(par(j) + 1))
res.sort()
for i in res:
    print(i)
