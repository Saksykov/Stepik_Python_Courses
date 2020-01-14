# Old LCD calculator
a1 = ' -- '
a2 = '|  |'
a3 = '    '
a4 = '   |'
a5 = '|   '

d = {'0': [a1, a2, a2, a3, a2, a2, a1],
     '1': [a3, a4, a4, a3, a4, a4, a3],
     '2': [a1, a4, a4, a1, a5, a5, a1],
     '3': [a1, a4, a4, a1, a4, a4, a1],
     '4': [a3, a2, a2, a1, a4, a4, a3],
     '5': [a1, a5, a5, a1, a4, a4, a1],
     '6': [a1, a5, a5, a1, a2, a2, a1],
     '7': [a1, a4, a4, a3, a4, a4, a3],
     '8': [a1, a2, a2, a1, a2, a2, a1],
     '9': [a1, a2, a2, a1, a4, a4, a1]}

number = input()
#  number = '0123456789'
n = len(number)
matrix = [[d[s][i] for s in number] for i in range(7)]
frame = '|'

print('x' + '-' * (5 * n - 1) + 'x')
for i in range(7):
    print(frame, end='')
    print(*matrix[i], end='')
    print(frame)
print('x' + '-' * (5 * n - 1) + 'x')