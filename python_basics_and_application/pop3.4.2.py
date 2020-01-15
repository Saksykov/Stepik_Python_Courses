'''
Вашей программе на вход подается ссылка на HTML файл.
Вам необходимо скачать этот файл, затем найти в нем все ссылки вида <a ... href="..." ... >
и вывести список сайтов, на которые есть ссылка.
'''
import re
import requests

f = input().rstrip()
res = requests.get(f)
t = res.text
p = r'<a.*href="?\'?(?:\w+:\/+)?(?:\.*)([\w.-]*)'
a = re.findall(p, t)
a = set(a)
a = list(a)
a.sort()
for i in a:
    print(i)