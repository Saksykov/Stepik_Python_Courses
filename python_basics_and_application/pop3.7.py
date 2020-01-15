'''
Вам дано описание пирамиды из кубиков в формате XML.
Кубики могут быть трех цветов: красный (red), зеленый (green) и синий (blue﻿).
Для каждого кубика известны его цвет, и известны кубики, расположенные прямо под ним.
'''
from xml.etree import ElementTree

d = {'red': 0, 'green': 0, 'blue': 0}

xml = input().strip()
root = ElementTree.fromstring(xml)
if root.tag == 'cube' and root.attrib['color'] in d:
    d[root.attrib['color']] += 1

for col in d:
    cnt = 2
    al = root.findall('.//cube[@color=\'' + col + '\']')
    n = len(al)
    s = './cube[@color=\'' + col + '\']'
    while n > 0:
        ch = root.findall(s)
        if len(ch) > 0:
            d[col] += cnt * len(ch)
            n -= len(ch)
        cnt += 1
        s = s.replace('.', './cube')
print(d['red'], d['green'], d['blue'])