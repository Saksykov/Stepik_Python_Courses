'''
Регулярные выражения в Python
'''
import sys
import re

for line in sys.stdin:
    line = line.rstrip()
    reg = r'\\'
    if re.search(reg, line):
        print(line)