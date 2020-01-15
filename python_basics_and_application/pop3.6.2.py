'''
В этой задаче вам необходимо воспользоваться API сайта artsy.net

API проекта Artsy предоставляет информацию о некоторых деятелях искусства, их работах, выставках.

В рамках данной задачи вам понадобятся сведения о деятелях искусства (назовем их, условно, художники).

Вам даны идентификаторы художников в базе Artsy.
Для каждого идентификатора получите информацию о имени художника и годе рождения.
Выведите имена художников в порядке неубывания года рождения. В случае если у художников одинаковый год рождения,
выведите их имена в лексикографическом порядке.
'''
import requests
import json
import sys

client_id = 'f2737d5f2486e80e4aa2'
client_secret = '88b5a503c6923fa36a04ec164fe961f7'

r = requests.post("https://api.artsy.net/api/tokens/xapp_token",
                  data={
                      "client_id": client_id,
                      "client_secret": client_secret
                  })
j = json.loads(r.text)
token = j["token"]
headers = {'X-Xapp-Token': token}
url = 'https://api.artsy.net/api/artists/'
s = []
while True:
    name = input().strip()
    if name == '':
        break
    res = requests.get(url + name, headers=headers).json()
    s.append(res['birthday'] + ' ' + res['sortable_name'])
s.sort()
for i in s:
    print(i[5:])
