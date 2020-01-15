'''
Регулярные выражения в Python
'''
import sys
import re

for line in sys.stdin:
    line = line.strip()
    reg = r'cat'
    if len(re.findall(reg, line)) >= 2:
        print(line)