# Length translator
d = {'m': 1, 'mile': 1609, 'yard': 0.9144, 'foot': 0.3048, 'inch': 0.0254, 'km': 1000, 'cm': 0.01, 'mm': 0.001}
s = ([str(i) for i in input().split()])
print("{:.2e}".format(float(s[0]) * d[s[1]] / d[s[3]]))