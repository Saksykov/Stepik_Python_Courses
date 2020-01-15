import requests

with open(r'D:\dataset_3378_2.txt', 'r') as fileName:
    for i in fileName:
        fn = i.strip()
res = requests.get(fn).text
res = res.splitlines()
cnt = 0
for i in res:
    cnt += 1
print(cnt)