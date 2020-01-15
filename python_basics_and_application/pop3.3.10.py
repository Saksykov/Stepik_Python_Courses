'''
Вам дана последовательность строк.
Выведите строки, содержащие двоичную запись числа, кратного 3.
'''

import sys
import re

for line in sys.stdin:
    line = line.rstrip()
    pat = r'^((1(01*0)*1|0)*)$'
    if re.findall(pat, line):
        print(line)