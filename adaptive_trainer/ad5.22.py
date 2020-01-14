# Anagram
a = input().strip().lower()
a = list(a)
b = input().strip().lower()
b = list(b)
f = True
if len(a) == len(b):
    for i in a:
        try:
            b.remove(i)
        except ValueError:
            f = False
            break
else:
    f = False
print(f)

# print(sorted(input().strip().lower()) == sorted(input().strip().lower()))