'''
Вашей программе на вход подаются две строки, содержащие url двух документов A и B.
Выведите Yes, если из A в B можно перейти за два перехода, иначе выведите No.
'''
import re
import requests

A = input().rstrip()
B = input().rstrip()

res = requests.get(A)
t = res.text
pat = r'<a href="?\'?([^"\'>]*)'
h = re.findall(pat, t)
fl = False
for i in h:
    res = requests.get(i)
    g = re.findall(pat, res.text)
    for j in g:
        if B == j:
            print('Yes')
            fl = True
            break
    if fl:
        break
if not fl:
    print('No')