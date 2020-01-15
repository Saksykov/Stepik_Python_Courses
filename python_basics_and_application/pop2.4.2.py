import os.path

res = []
for cur_dir, dir, file in os.walk(r'D:\main'):
    for i in file:
        if i.endswith('.py'):
            res.append(cur_dir.strip()[3::])
            break

r = '\n'.join(res)
with open(r'D:\write.txt', 'w') as w:
    w.write(r)