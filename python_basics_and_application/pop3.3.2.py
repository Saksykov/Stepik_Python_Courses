'''
Регулярные выражения в Python
'''
import sys
import re

for line in sys.stdin:
    line = line.strip()
    reg = r'\bcat\b'
    if re.search(reg, line):
        print(line)