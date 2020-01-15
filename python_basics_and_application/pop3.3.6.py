'''
Регулярные выражения в Python
'''
import sys
import re

for line in sys.stdin:
    line = line.rstrip()
    a = r'computer'
    b = r'human'
    print(re.sub(b, a, line))