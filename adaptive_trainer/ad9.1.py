# Durak
c = {'6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
f, s = (str(i) for i in input().split())
coz = str(input())
if f[-1] == s[-1]:
    if c.get(f[:-1]) > c.get(s[:-1]):
        print('First')
    elif c.get(f[:-1]) < c.get(s[:-1]):
        print('Second')
    else:
        print('Error')
else:
    if f[-1] == coz:
        print('First')
    elif s[-1] == coz:
        print('Second')
    else:
        print('Error')
