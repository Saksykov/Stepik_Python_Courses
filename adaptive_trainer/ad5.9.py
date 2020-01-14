# Fizz Buzz
a, b = (int(i) for i in input().split())
for i in range(a, b+1):
    if i % 15 == 0:
        print('FizzBuzz')
        continue
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)