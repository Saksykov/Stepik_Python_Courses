"""
Файл https://stepik.org/media/attachments/lesson/209719/2.html содержит статью с Википедии про язык Python.
В этой статье есть теги code, которыми выделяются конструкции на языке Python. Вам нужно найти все строки,
содержащиеся между тегами <code> и </code> и найти те строки, которые встречаются чаще всего и
вывести их в алфавитном порядке, разделяя пробелами.
"""
import re
from urllib.request import urlopen


html = urlopen("https://stepik.org/media/attachments/lesson/209719/2.html").read().decode("utf-8")
str_html = str(html)
ar = re.findall(r"<code>[\w\d _.,]+<\/code>", str_html)
d = {}
for a in ar:
    a = a[6:-7]
    if a in d:
        d[a] += 1
    else:
        d[a] = 1

max_val = max(d.values())
res = []
for i in d:
    if d[i] == max_val:
        res.append(i)

res.sort()
for i in res:
    print(i, end=" ")
