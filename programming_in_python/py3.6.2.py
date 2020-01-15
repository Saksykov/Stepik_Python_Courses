import requests
fn = 'https://stepic.org/media/attachments/course67/3.6.3/699991.txt'
st = 'https://stepic.org/media/attachments/course67/3.6.3/'
while True:
    res = requests.get(fn).text.split()
    if res[0].startswith('We'):
        print(fn)
        break
    else:
        fn = st + ''.join(res)
for i in res:
    print(i, end=' ')