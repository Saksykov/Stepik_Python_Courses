'''
Вам дана последовательность строк.
В каждой строке замените все вхождения нескольких одинаковых букв на одну букву.
Буквой считается символ из группы \w.
'''

import sys
import re

for line in sys.stdin:
    line = line.rstrip()
    a = r'(\w)\1+'
    print(re.sub(a, r'\1', line))