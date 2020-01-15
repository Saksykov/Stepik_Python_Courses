'''
Регулярные выражения в Python
'''
import sys
import re

for line in sys.stdin:
    line = line.strip()
    reg = r'z(.{3})z'
    if re.search(reg, line):
        print(line)