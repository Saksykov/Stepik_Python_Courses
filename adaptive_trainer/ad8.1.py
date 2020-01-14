s = []
s.extend(str(i) for i in input().split())
if s[1] == 'plus':
    print(int(s[0]) + int(s[2]))
elif s[1] == 'minus':
    print(int(s[0]) - int(s[2]))
elif s[1] == 'multiply':
    print(int(s[0]) * int(s[2]))
else:
    if s[2] != '0':
        print(int(s[0]) // int(s[2]))