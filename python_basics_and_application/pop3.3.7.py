'''
Регулярные выражения в Python
'''
import sys
import re

for line in sys.stdin:
    line = line.rstrip()
    a = r'argh'
    b = r'\b(a|A)+\b'
    print(re.sub(b, a, line, count=1))