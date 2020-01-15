# Работа с файловой системой и файлами
s = []
with open(r'D:\dataset_24465_4.txt', 'r') as r, open(r'D:\write.txt', 'w') as w:
    for i in r:
        s.append(i.strip())
    s.reverse()
    w.write('\n'.join(s))

